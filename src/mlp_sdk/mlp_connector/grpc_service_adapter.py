import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from queue import Queue
from time import perf_counter
from typing import Generator, List, MutableMapping, Optional, cast

from mlp_sdk.abstract.services import MlpException, MlpRequestContext
from mlp_sdk.mlp_connector.grpc_ import mlp_grpc_pb2
from mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2 import (
    BatchPayloadProto,
    BatchResponseProto,
    ExtendedResponseProto,
    GateToServiceProto,
    PartialPredictResponseProto,
    PayloadProto,
    PredictResponseProto,
    ServiceToGateProto,
)
from mlp_sdk.mlp_connector.grpc_service_base import MlpGrpcServiceBase
from mlp_sdk.mlp_connector.multi_host_connector import MlpGrpcRequestReceiver, MlpGrpcResponseReceiver
from mlp_sdk.utils.config import get_config
from mlp_sdk.utils.logger import get_logger

log = get_logger("MlpGrpcServiceAdapter")
config = get_config()


@dataclass
class ContextAndStream:
    context: MlpRequestContext
    stream: Queue[GateToServiceProto]


class MlpGrpcServiceAdapter(MlpGrpcRequestReceiver):
    def __init__(self, service: MlpGrpcServiceBase):
        self.response_receiver: MlpGrpcResponseReceiver
        self.impl = service
        self.request_streams: dict[int, ContextAndStream] = {}  # список очередей для стримминговыз запросов
        self.thread_pool = ThreadPoolExecutor(max_workers=config.sdk.requests_executor_pool_size, thread_name_prefix="worker-")

    def set_response_receiver(self, response_receiver: MlpGrpcResponseReceiver):
        self.response_receiver = response_receiver

    def message_from_gate(self, context: MlpRequestContext, request: GateToServiceProto):
        # здесь мы получаем сообщение от GPRC-коннектора
        # на исходном потоке никакую обработку делать нельзя, потому что он в нашем grpc-коннекторе один
        # поэтому сразу перекладываем на тред-пул
        self.thread_pool.submit(self.__process_message_from_gate_with_log, context, request)

    def __process_message_from_gate_with_log(self, context: MlpRequestContext, message: GateToServiceProto):
        start_time = perf_counter()
        error_response = None
        try:
            self.__process_message_from_gate(context, message)
        except MlpException as e:
            log.error(f"Error when processing request {context.requestId}: {str(e)}", extra={"requestId": context.requestId})
            error_response = mlp_grpc_pb2.ServiceToGateProto(error=MlpGrpcServiceBase.mlp_exception_to_proto(e))
        except BaseException as e:
            log.exception(e, extra={"requestId": context.requestId})
            error_response = mlp_grpc_pb2.ServiceToGateProto(error=MlpGrpcServiceBase.exception_to_proto(e))

        if error_response:
            processing_time = round((time.perf_counter() - start_time) * 1000)  # to ms and round mathematically
            error_response.headers["Z-Server-Time"] = str(processing_time)
            self.response_receiver.message_from_service(context, error_response)

    def __process_message_from_gate(self, context: MlpRequestContext, message: GateToServiceProto):
        request_type = message.WhichOneof("body")

        if request_type == "predict":
            self.__process_simple_request(context, message.predict.data, message.predict.config)
        elif request_type == "ext":
            self.__process_ext_request(context, message.ext.methodName, message.ext.params)
        elif request_type == "batch":
            self.__process_batch_request(context, list(message.batch.data), message.batch.config)
        elif request_type == "fit":
            # TODO: support fit requests
            raise MlpException(code="mlp-action.common.internal-error", message="Request type is not supported yet")
        elif request_type == "partialPredict":
            # для случая partialRequest заведём специальный дикт с очередями и будем перекладывать сообщение туда.
            if message.partialPredict.start:
                self.__process_streaming_request(context, message)
            elif context.requestId in self.request_streams:
                self.request_streams[context.requestId].stream.put(message)
            else:
                log.error(f"partial request ignored for requestId: {context.requestId}")
        elif request_type == "cancel":
            # для cancel - выставим флаг cancelled в соответствующем контексте
            self.request_streams[message.cancel.requestIdToCancel].context.cancelled = True
        else:
            log.error(f"Unsupported request type {request_type}")
            raise MlpException(code="mlp-action.common.internal-error", message="Request type is not supported yet")

    def __process_streaming_request(self, context: MlpRequestContext, message: GateToServiceProto):
        input_streaming_queue: Queue[GateToServiceProto] = Queue()
        self.request_streams[context.requestId] = ContextAndStream(context, input_streaming_queue)
        input_streaming_queue.put(message)

        def input_stream_generator() -> Generator[PayloadProto, None, None]:
            finished = False
            while True:
                if finished:
                    break
                sc = self.request_streams[context.requestId]
                if sc:
                    if sc.context.cancelled:
                        break
                    x = sc.stream.get()
                    if x.partialPredict.finish:
                        finished = True

                    yield x.partialPredict.data
                else:
                    break

        try:
            self.__process_simple_request(context, input_stream_generator(), message.partialPredict.config)
        finally:
            del self.request_streams[context.requestId]

    def __process_simple_request(self, context: MlpRequestContext, request: PayloadProto | Generator[PayloadProto, None, None], config: Optional[PayloadProto]):
        # сначала разберём простой предикт

        start_time = perf_counter()  # Z-Server-Time будем выставлять только для простых predict-методов
        res = self.impl.predict(context, request, config)  # тут должна быть поддержка и других методов

        if isinstance(res, Generator):
            first = True
            previous = None
            next_item = None
            while True:
                previous = next_item
                next_item = next(res, None)

                if previous is None:
                    continue

                msg = ServiceToGateProto(
                    partialPredict=PartialPredictResponseProto(start=first, finish=next_item is None, data=previous),
                    headers=context.response_headers,
                )
                self.response_receiver.message_from_service(context, msg)
                first = False

                if next_item is None:
                    break
        else:
            res = cast(PayloadProto, res)
            processing_time = round((time.perf_counter() - start_time) * 1000)  # to ms and round mathematically
            context.response_headers["Z-Server-Time"] = str(processing_time)

            msg = ServiceToGateProto(predict=PredictResponseProto(data=res), headers=context.response_headers)

            self.response_receiver.message_from_service(context, msg)

    def __process_ext_request(self, context: MlpRequestContext, method_name: str, params: MutableMapping[str, PayloadProto]):
        res = self.impl.ext(context, method_name, dict(params))

        msg = ServiceToGateProto(ext=ExtendedResponseProto(data=res))

        self.response_receiver.message_from_service(context, msg)

    def __process_batch_request(self, context: MlpRequestContext, req: List[BatchPayloadProto], config: Optional[PayloadProto]):
        res = self.impl.predict_batch(context, req, config)

        msg = ServiceToGateProto(batch=BatchResponseProto(data=res))

        self.response_receiver.message_from_service(context, msg)
