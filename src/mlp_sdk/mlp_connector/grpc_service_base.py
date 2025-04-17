from typing import Generator, List, Optional

from mlp_sdk.abstract.services import MlpException, MlpRequestContext
from mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2 import (
    ApiErrorProto,
    BatchPayloadProto,
    BatchPayloadResponseProto,
    PayloadProto,
    PredictResponseProto,
    ServiceDescriptorProto,
    SimpleStatusProto,
)


class MlpGrpcServiceBase:
    def get_descriptor(self) -> ServiceDescriptorProto:
        return ServiceDescriptorProto(name=self.__class__.__name__, fittable=False, methods={}, schemaFiles={})

    def predict(
        self,
        context: MlpRequestContext,
        req: PayloadProto | Generator[PayloadProto, None, None],
        config: Optional[PayloadProto],
    ) -> PayloadProto | Generator[PayloadProto, None, None]:
        raise NotImplementedError()

    def ext(self, context: MlpRequestContext, method_name: str, params: dict[str, PayloadProto]) -> PayloadProto:
        raise MlpException(code="mlp-action.common.method-not-supported", message="Method not implemented.")

    def predict_batch(self, context: MlpRequestContext, req: List[BatchPayloadProto], config: Optional[PayloadProto]) -> List[BatchPayloadResponseProto]:
        result: List[BatchPayloadResponseProto] = []
        for x in req:
            context_per_request = MlpRequestContext(requestId=x.requestId, gatewayId=context.gatewayId, request_headers=context.request_headers)
            res: PayloadProto | None = None
            error: ApiErrorProto | None = None
            try:
                rr = self.predict(context=context_per_request, req=x.data, config=config)
                if not isinstance(rr, PayloadProto):
                    raise Exception("Predict must not return streaming result to use in batch mode")
                res = rr
            except MlpException as e:
                error = self.mlp_exception_to_proto(e)
            except BaseException as e:
                error = self.exception_to_proto(e)

            result.append(
                BatchPayloadResponseProto(
                    requestId=x.requestId, predict=PredictResponseProto(data=res), error=error, headers=context_per_request.response_headers
                )
            )

        return result

    @staticmethod
    def mlp_exception_to_proto(e: MlpException):
        return ApiErrorProto(code=e.code, message=e.message, status=e.status.to_proto(), args=e.named_args)

    @staticmethod
    def exception_to_proto(e: BaseException):
        return ApiErrorProto(code="mlp-action.common.internal-error", message=str(e), status=SimpleStatusProto.INTERNAL_SERVER_ERROR, args={})
