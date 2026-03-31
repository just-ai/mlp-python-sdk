import time
from typing import Generator, Optional

from mlp_sdk.abstract.services import MlpException, MlpRequestContext
from mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2 import (
    BatchPayloadProto,
    BatchRequestProto,
    CancelRequestProto,
    ExtendedRequestProto,
    FitRequestProto,
    GateToServiceProto,
    PartialPredictRequestProto,
    PayloadProto,
    PredictRequestProto,
    ServiceToGateProto,
)
from mlp_sdk.mlp_connector.grpc_service_adapter import MlpGrpcServiceAdapter
from mlp_sdk.mlp_connector.grpc_service_base import MlpGrpcServiceBase
from mlp_sdk.mlp_connector.multi_host_connector import MlpGrpcResponseReceiver
from mlp_sdk.utils.json_ import JSON
from mlp_sdk.utils.utils import wait_for


class ImplSimple(MlpGrpcServiceBase):
    def predict(
        self, context: MlpRequestContext, req: PayloadProto | Generator[PayloadProto, None, None], config: Optional[PayloadProto]
    ) -> PayloadProto | Generator[PayloadProto, None, None]:
        if req.json == '"error"':
            raise MlpException(code="error", message="bad things")
        if req.json == '"error1"':
            raise Exception("Bad thins happened")
        return PayloadProto(json='"test"')


class ImplOutputStream(MlpGrpcServiceBase):
    def predict(
        self, context: MlpRequestContext, req: PayloadProto | Generator[PayloadProto, None, None], config: Optional[PayloadProto]
    ) -> PayloadProto | Generator[PayloadProto, None, None]:
        data = [PayloadProto(json="1"), PayloadProto(json="2"), PayloadProto(json="3")]
        return (y for y in data)


class ImplInputStream(MlpGrpcServiceBase):
    def predict(
        self, context: MlpRequestContext, req: PayloadProto | Generator[PayloadProto, None, None], config: Optional[PayloadProto]
    ) -> PayloadProto | Generator[PayloadProto, None, None]:
        res = [x.json for x in req]
        return PayloadProto(json=JSON.stringify(res))


class ImplExt(MlpGrpcServiceBase):
    def ext(self, context: MlpRequestContext, method_name: str, params: dict[str, PayloadProto]) -> PayloadProto:
        return PayloadProto(json='"ext"')


class TestMlpGrpcServiceAdapter(MlpGrpcResponseReceiver):
    def message_from_service(self, context: MlpRequestContext, response: ServiceToGateProto) -> None:
        self.response.append(response)

    def init(self, impl):
        self.impl = impl
        self.adapter = MlpGrpcServiceAdapter(impl)
        self.adapter.set_response_receiver(self)
        self.context = MlpRequestContext(requestId=1, gatewayId="test", request_headers={}, response_headers={})
        self.response = []

    def teardown_method(self):
        self.adapter.shutdown()

    def wait_for(self, condition, timeout=5):
        """Wait for a condition to be true with a timeout."""
        start_time = time.time()
        counter = 1
        while not condition() and time.time() - start_time < timeout:
            if counter % 10 == 0:
                print(f"Waiting for condition {condition} ...")
            time.sleep(0.1)
            counter += 1
        return condition()

    def test_thread_pool(self):
        self.init(ImplSimple())
        self.adapter.message_from_gate(self.context, GateToServiceProto(predict=PredictRequestProto(data=PayloadProto(json="{}"))))

        wait_for(lambda: len(self.response) == 1)

    def test_predict_simple(self):
        self.init(ImplSimple())
        self.adapter.message_from_gate(self.context, GateToServiceProto(predict=PredictRequestProto(data=PayloadProto(json="{}"))))

        wait_for(lambda: len(self.response) == 1)
        res: ServiceToGateProto = self.response[0]
        assert res.predict.data.json == '"test"'

    def test_ext(self):
        self.init(ImplExt())
        self.adapter.message_from_gate(
            self.context, GateToServiceProto(ext=ExtendedRequestProto(methodName="test", params={"param": PayloadProto(json="{}")}))
        )

        wait_for(lambda: len(self.response) == 1)
        res: ServiceToGateProto = self.response[0]
        assert res.ext.data.json == '"ext"'

    def test_batch(self):
        self.init(ImplSimple())
        batch_data = [BatchPayloadProto(requestId=1, data=PayloadProto(json="{}")), BatchPayloadProto(requestId=2, data=PayloadProto(json="{}"))]
        self.adapter.message_from_gate(self.context, GateToServiceProto(batch=BatchRequestProto(data=batch_data)))

        wait_for(lambda: len(self.response) == 1)
        res: ServiceToGateProto = self.response[0]
        assert len(res.batch.data) == 2
        assert res.batch.data[0].predict.data.json == '"test"'
        assert res.batch.data[1].predict.data.json == '"test"'

    def test_error_in_batch(self):
        self.init(ImplSimple())
        batch_data = [
            BatchPayloadProto(requestId=1, data=PayloadProto(json="{}")),
            BatchPayloadProto(requestId=2, data=PayloadProto(json='"error"')),
            BatchPayloadProto(requestId=3, data=PayloadProto(json='"error1"')),
        ]
        self.adapter.message_from_gate(self.context, GateToServiceProto(batch=BatchRequestProto(data=batch_data)))

        wait_for(lambda: len(self.response) == 1)
        res: ServiceToGateProto = self.response[0]
        assert len(res.batch.data) == 3
        assert res.batch.data[0].predict.data.json == '"test"'
        assert res.batch.data[1].error.code == "error"
        assert res.batch.data[1].error.message == "bad things"
        # assert res.batch.data[2].error.code == '??'
        assert res.batch.data[2].error.message == "Bad thins happened"

    def test_fit_not_supported(self):
        self.init(ImplSimple())
        self.adapter.message_from_gate(self.context, GateToServiceProto(fit=FitRequestProto()))

        wait_for(lambda: len(self.response) == 1)
        res: ServiceToGateProto = self.response[0]
        assert res.WhichOneof("body") == "error"
        assert res.error.code == "mlp-action.common.internal-error"

    def test_output_stream(self):
        self.init(ImplOutputStream())
        self.adapter.message_from_gate(self.context, GateToServiceProto(predict=PredictRequestProto(data=PayloadProto(json="{}"))))

        wait_for(lambda: len(self.response) == 4)
        assert self.response[0].partialPredict.data.json == "1"
        assert self.response[0].partialPredict.start
        assert not self.response[0].partialPredict.finish

        assert self.response[1].partialPredict.data.json == "2"
        assert not self.response[1].partialPredict.start
        assert not self.response[1].partialPredict.finish

        assert self.response[2].partialPredict.data.json == "3"
        assert not self.response[2].partialPredict.start
        assert not self.response[2].partialPredict.finish

        assert not self.response[3].partialPredict.data.json
        assert not self.response[3].partialPredict.start
        assert self.response[3].partialPredict.finish

    def test_input_stream(self):
        self.init(ImplInputStream())

        # Create a context with a unique request ID for this test
        stream_context = MlpRequestContext(requestId=999, gatewayId="test", request_headers={}, response_headers={})

        def send_partial(message, start=False, finish=False):
            """Helper function to send partial predict messages"""
            self.adapter.message_from_gate(
                stream_context,
                GateToServiceProto(partialPredict=PartialPredictRequestProto(data=PayloadProto(json=f'"{message}"'), start=start, finish=finish)),
            )

        # Send start message
        send_partial("message1", start=True)

        # Send middle messages
        send_partial("message2")
        send_partial("message3")

        # Send finish message
        send_partial("message4", finish=True)

        # Wait for processing to complete
        wait_for(lambda: len(self.response) > 0, timeout=5)

        # Check the result
        assert len(self.response) == 1
        res = self.response[0]
        assert res.predict.data.json.find("message1") >= 0
        assert res.predict.data.json.find("message2") >= 0
        assert res.predict.data.json.find("message3") >= 0
        assert res.predict.data.json.find("message4") >= 0

    def test_input_stream_wrong_message_id(self):
        self.init(ImplSimple())

        # Create a context with a unique request ID for this test
        stream_context = MlpRequestContext(requestId=997, gatewayId="test", request_headers={}, response_headers={})

        def send_partial(message, start=False, finish=False):
            """Helper function to send partial predict messages"""
            self.adapter.message_from_gate(
                stream_context,
                GateToServiceProto(partialPredict=PartialPredictRequestProto(data=PayloadProto(json=f'"{message}"'), start=start, finish=finish)),
            )

        # Send start message
        send_partial("message1", start=False)
        send_partial("message1", start=False)

    def test_cancelation(self):
        class SlowStreamImpl(MlpGrpcServiceBase):
            def predict(
                self, context: MlpRequestContext, req: PayloadProto | Generator[PayloadProto, None, None], config: Optional[PayloadProto]
            ) -> PayloadProto | Generator[PayloadProto, None, None]:
                def generate_slow_stream():
                    for i in range(10):
                        if context.cancelled:
                            break
                        yield PayloadProto(json=f'"{i}"')
                        time.sleep(0.1)  # Sleep 100ms between messages

                return generate_slow_stream()

        self.init(SlowStreamImpl())

        # Create a context with a unique request ID for this test
        stream_context = MlpRequestContext(requestId=888, gatewayId="test", request_headers={}, response_headers={})

        # Send the request
        self.adapter.message_from_gate(stream_context, GateToServiceProto(predict=PredictRequestProto(data=PayloadProto(json="{}"))))

        # Wait for at least one response
        wait_for(lambda: len(self.response) >= 1, timeout=2)

        # Send cancellation request
        self.adapter.message_from_gate(stream_context, GateToServiceProto(cancel=CancelRequestProto(requestIdToCancel=888)))

        # Wait a bit to allow for some more processing
        time.sleep(1.5)

        # Check that we received fewer than 10 responses (should be cancelled)
        assert len(self.response) < 10

    def test_input_stream_ordering(self):
        """Verify that streaming continuation messages preserve arrival order.

        Regression test: ThreadPoolExecutor(max_workers=10) was dispatching continuation
        messages to worker threads, causing queue.put() calls to race when messages
        arrived in bursts (same millisecond). Adjacent tokens would swap positions.
        """

        class OrderedInputStream(MlpGrpcServiceBase):
            def predict(
                self, context: MlpRequestContext, req: PayloadProto | Generator[PayloadProto, None, None], config: Optional[PayloadProto]
            ) -> PayloadProto | Generator[PayloadProto, None, None]:
                return PayloadProto(json=JSON.stringify([x.json for x in req]))

        self.init(OrderedInputStream())

        stream_context = MlpRequestContext(requestId=777, gatewayId="test", request_headers={}, response_headers={})
        tokens = [f"token_{i}" for i in range(50)]

        # Send start
        self.adapter.message_from_gate(
            stream_context,
            GateToServiceProto(partialPredict=PartialPredictRequestProto(data=PayloadProto(json=f'"{tokens[0]}"'), start=True)),
        )

        # Send continuation messages as fast as possible to trigger the race
        for token in tokens[1:-1]:
            self.adapter.message_from_gate(
                stream_context,
                GateToServiceProto(partialPredict=PartialPredictRequestProto(data=PayloadProto(json=f'"{token}"'))),
            )

        # Send finish
        self.adapter.message_from_gate(
            stream_context,
            GateToServiceProto(partialPredict=PartialPredictRequestProto(data=PayloadProto(json=f'"{tokens[-1]}"'), finish=True)),
        )

        wait_for(lambda: len(self.response) > 0, timeout=5)

        assert len(self.response) == 1
        result = JSON.parse_(self.response[0].predict.data.json)
        expected = [f'"{t}"' for t in tokens]
        assert result == expected, f"Token order mismatch: expected {expected}, got {result}"

    def test_cancellation_wrong_id(self):
        self.init(ImplSimple())

        # Create a context with a unique request ID for this test
        self.adapter.message_from_gate(self.context, GateToServiceProto(cancel=CancelRequestProto(requestIdToCancel=99)))
