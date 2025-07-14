from typing import Generator, List, Optional

from mlp_sdk.abstract.services import MlpErrorStatus, MlpException, MlpRequestContext
from mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2 import (
    ApiErrorProto,
    BatchPayloadProto,
    BatchPayloadResponseProto,
    PayloadProto,
    PredictResponseProto,
    ServiceDescriptorProto,
)


class MlpGrpcServiceBase:
    def get_descriptor(self) -> ServiceDescriptorProto:  # pragma: no cover
        # TODO: implement it sometime
        return ServiceDescriptorProto(name=self.__class__.__name__, fittable=False, methods={}, schemaFiles={})

    def predict(
        self,
        context: MlpRequestContext,
        req: PayloadProto | Generator[PayloadProto, None, None],
        config: Optional[PayloadProto],
    ) -> PayloadProto | Generator[PayloadProto, None, None]:
        raise NotImplementedError()  # pragma: no cover

    def ext(self, context: MlpRequestContext, method_name: str, params: dict[str, PayloadProto]) -> PayloadProto:
        raise MlpException(
            code="mlp-action.common.method-not-supported", message="Method not implemented.", status=MlpErrorStatus.BAD_REQUEST
        )  # pragma: no cover

    def predict_batch(self, context: MlpRequestContext, req: List[BatchPayloadProto], config: Optional[PayloadProto]) -> List[BatchPayloadResponseProto]:
        result: List[BatchPayloadResponseProto] = []
        for x in req:
            context_per_request = MlpRequestContext(requestId=x.requestId, gatewayId=context.gatewayId, request_headers=context.request_headers)
            res: PayloadProto | None = None
            error: ApiErrorProto | None = None
            try:
                rr = self.predict(context=context_per_request, req=x.data, config=config)
                if not isinstance(rr, PayloadProto):
                    raise Exception("Predict must not return streaming result to use in batch mode")  # pragma: no cover
                res = rr
            except BaseException as e:
                error = MlpException.exception_to_proto(e)

            result.append(
                BatchPayloadResponseProto(
                    requestId=x.requestId, predict=PredictResponseProto(data=res), error=error, headers=context_per_request.response_headers
                )
            )

        return result
