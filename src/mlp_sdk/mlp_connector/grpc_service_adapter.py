import functools
import time
from collections.abc import Generator as GeneratorABC
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from dataclasses import dataclass
from queue import Queue
from time import perf_counter
from typing import Generator, List, MutableMapping, Optional, cast

from mlp_sdk.abstract.services import MlpErrorStatus, MlpException, MlpRequestContext
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
    stream: Queue[GateToServiceProto] | None


class MlpGrpcServiceAdapter(MlpGrpcRequestReceiver):
    def __init__(self, service: MlpGrpcServiceBase):
        self.response_receiver: MlpGrpcResponseReceiver
        self.impl = service
        self.request_streams: dict[int, ContextAndStream] = {}  # список очередей для стримминговых запросов
        self.thread_pool = ThreadPoolExecutor(max_workers=config.sdk.requests_executor_pool_size, thread_name_prefix="worker-")

    def shutdown(self):
        self.thread_pool.shutdown()

    def set_response_receiver(self, response_receiver: MlpGrpcResponseReceiver):
        self.response_receiver = response_receiver

    def message_from_gate(self, context: MlpRequestContext, request: GateToServiceProto):
        self.__process_message_from_gate(context, request)

    @contextmanager
    def _request_scope(self, context: MlpRequestContext):
        start_time = perf_counter()
        try:
            yield
        except BaseException as e:
            log.exception(f"Error when processing request {context.requestId}: {str(e)}", extra={"requestId": context.requestId})

            processing_time = round((time.perf_counter() - start_time) * 1000)  # to ms and round mathematically
            error_response = mlp_grpc_pb2.ServiceToGateProto(error=MlpException.exception_to_proto(e))
            error_response.headers["Z-Server-Time"] = str(processing_time)

            self.response_receiver.message_from_service(context, error_response)

    @staticmethod
    def _with_request_scope(method):
        """Декоратор: оборачивает метод в _request_scope. Первый аргумент после self — context."""

        @functools.wraps(method)
        def wrapper(self, context, *args, **kwargs):
            with self._request_scope(context):
                return method(self, context, *args, **kwargs)

        return wrapper

    def __process_message_from_gate(self, context: MlpRequestContext, request: GateToServiceProto):
        # Поток коннектора — один, поэтому тяжёлые операции (predict, ext, batch, streaming start)
        # уходят в thread pool. Лёгкие операции (continuation queue.put, cancel flag) выполняются
        # inline, чтобы сохранить порядок токенов при burst-поступлении.
        request_type = request.WhichOneof("body")

        if request_type == "predict":
            self.thread_pool.submit(self.__process_simple_request, context, request.predict.data, request.predict.config)
        elif request_type == "ext":
            self.thread_pool.submit(self.__process_ext_request, context, request.ext.methodName, request.ext.params)
        elif request_type == "batch":
            self.thread_pool.submit(self.__process_batch_request, context, list(request.batch.data), request.batch.config)
        elif request_type == "fit":
            # TODO: support fit requests
            self.thread_pool.submit(self.__process_unsupported_request, context, "Request type is not supported yet")
        elif request_type == "partialPredict":
            if request.partialPredict.start:
                # Создаём очередь и запись в request_streams inline (на потоке коннектора),
                # чтобы continuation-сообщения, пришедшие сразу после start, не потерялись.
                input_streaming_queue: Queue[GateToServiceProto] = Queue()
                self.request_streams[context.requestId] = ContextAndStream(context, input_streaming_queue)
                input_streaming_queue.put(request)
                self.thread_pool.submit(self.__process_streaming_request, context, input_streaming_queue, request.partialPredict.config)
            else:
                # continuation-сообщения выполняются inline на потоке коннектора —
                # queue.put() неблокирующий, а через thread pool порядок токенов ломается при burst-поступлении.
                with self._request_scope(context):
                    cs = self.request_streams.get(context.requestId)
                    if cs is not None and cs.stream is not None:
                        cs.stream.put(request)
                    else:
                        log.error(f"partial request ignored for requestId: {context.requestId}")  # pragma: no cover
        elif request_type == "cancel":
            with self._request_scope(context):
                cs = self.request_streams.get(request.cancel.requestIdToCancel)
                if cs is not None:
                    cs.context.cancelled = True
                else:
                    log.error(f"cancellation request ignored for requestIdToCancel: {request.cancel.requestIdToCancel}")
        else:
            self.thread_pool.submit(  # pragma: no cover
                self.__process_unsupported_request, context, "Unknown request type. Probably there is a client-server version missmatch"
            )

    @_with_request_scope
    def __process_unsupported_request(self, context: MlpRequestContext, message: str):
        raise MlpException(code="mlp-action.common.internal-error", message=message, status=MlpErrorStatus.BAD_REQUEST)

    @_with_request_scope
    def __process_streaming_request(
        self, context: MlpRequestContext, input_streaming_queue: Queue[GateToServiceProto], config: Optional[PayloadProto]
    ):
        def input_stream_generator() -> Generator[PayloadProto, None, None]:
            finished = False
            while not finished:
                x = input_streaming_queue.get()
                if x.partialPredict.finish:
                    finished = True
                yield x.partialPredict.data

        self.__process_simple_request(context, input_stream_generator(), config)

    @_with_request_scope
    def __process_simple_request(
        self,
        context: MlpRequestContext,
        request: PayloadProto | Generator[PayloadProto, None, None],
        config: Optional[PayloadProto],
    ):
        start_time = perf_counter()  # Z-Server-Time будем выставлять только для простых predict-методов
        res = self.impl.predict(context, request, config)  # тут должна быть поддержка и других методов

        if isinstance(res, GeneratorABC):
            if context.requestId not in self.request_streams:
                self.request_streams[context.requestId] = ContextAndStream(context, None)
            try:
                first = True
                current_chunk = None
                while True:
                    current_chunk = next(res, None)
                    msg = ServiceToGateProto(
                        partialPredict=PartialPredictResponseProto(start=first, finish=current_chunk is None, data=current_chunk),
                        headers=context.response_headers,
                    )
                    self.response_receiver.message_from_service(context, msg)
                    first = False
                    if current_chunk is None:
                        break
            finally:
                if context.requestId in self.request_streams:
                    del self.request_streams[context.requestId]
        else:
            res = cast(PayloadProto, res)
            processing_time = round((time.perf_counter() - start_time) * 1000)  # to ms and round mathematically
            context.response_headers["Z-Server-Time"] = str(processing_time)

            msg = ServiceToGateProto(predict=PredictResponseProto(data=res), headers=context.response_headers)

            self.response_receiver.message_from_service(context, msg)

    @_with_request_scope
    def __process_ext_request(self, context: MlpRequestContext, method_name: str, params: MutableMapping[str, PayloadProto]):
        res = self.impl.ext(context, method_name, dict(params))

        msg = ServiceToGateProto(ext=ExtendedResponseProto(data=res))

        self.response_receiver.message_from_service(context, msg)

    @_with_request_scope
    def __process_batch_request(self, context: MlpRequestContext, req: List[BatchPayloadProto], config: Optional[PayloadProto]):
        res = self.impl.predict_batch(context, req, config)

        msg = ServiceToGateProto(batch=BatchResponseProto(data=res))

        self.response_receiver.message_from_service(context, msg)
