import time
from typing import Generator, Optional

from mlp_sdk.abstract.services import MlpRequestContext
from mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2 import GateToServiceProto, PayloadProto, PredictRequestProto, ServiceToGateProto
from mlp_sdk.mlp_connector.grpc_service_adapter import MlpGrpcServiceAdapter
from mlp_sdk.mlp_connector.grpc_service_base import MlpGrpcServiceBase
from mlp_sdk.mlp_connector.multi_host_connector import MlpGrpcResponseReceiver


class TestImplSimple(MlpGrpcServiceBase):
    def predict(
        self, context: MlpRequestContext, req: PayloadProto | Generator[PayloadProto, None, None], config: Optional[PayloadProto]
    ) -> PayloadProto | Generator[PayloadProto, None, None]:
        return PayloadProto(json='"test"')


class TestImplStream(MlpGrpcServiceBase):
    def predict(
        self, context: MlpRequestContext, req: PayloadProto | Generator[PayloadProto, None, None], config: Optional[PayloadProto]
    ) -> PayloadProto | Generator[PayloadProto, None, None]:
        data = [PayloadProto(json="1"), PayloadProto(json="2"), PayloadProto(json="3")]
        return (y for y in data)


class TestImplExt(MlpGrpcServiceBase):
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
        self.init(TestImplSimple())
        self.adapter.message_from_gate(self.context, GateToServiceProto(predict=PredictRequestProto(data=PayloadProto(json="{}"))))

        self.wait_for(lambda: len(self.response) == 1)

    def test_predict_simple(self):
        self.init(TestImplSimple())
        self.adapter._process_message_from_gate_with_log(self.context, GateToServiceProto(predict=PredictRequestProto(data=PayloadProto(json="{}"))))

        assert len(self.response) == 1
        res: ServiceToGateProto = self.response[0]
        assert res.predict.data.json == '"test"'
