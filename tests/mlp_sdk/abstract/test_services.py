import pytest

from mlp_sdk.abstract.services import MlpErrorStatus, MlpException
from mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2 import SimpleStatusProto


def test_from_proto():
    # Test conversion from proto with OK status
    ss = SimpleStatusProto.INTERNAL_SERVER_ERROR
    assert MlpErrorStatus.from_proto(ss) == MlpErrorStatus.INTERNAL_SERVER_ERROR


# Upstream/transient error statuses that the wire format (SimpleStatusProto) has always
# supported but MlpErrorStatus did not expose. Without them, e.g. an upstream 503 could
# only be reported as a generic 500 (mlp-action.common.internal-error).
@pytest.mark.parametrize(
    "status",
    [
        MlpErrorStatus.TOO_MANY_REQUESTS,
        MlpErrorStatus.BAD_GATEWAY,
        MlpErrorStatus.SERVICE_UNAVAILABLE,
        MlpErrorStatus.GATEWAY_TIMEOUT,
    ],
)
def test_upstream_error_statuses_roundtrip(status):
    proto = status.to_proto()
    assert proto == getattr(SimpleStatusProto, status.name)
    assert MlpErrorStatus.from_proto(proto) == status


def test_service_unavailable_exception_to_proto():
    res = MlpException.exception_to_proto(
        MlpException(
            code="mlp-action.common.service-unavailable",
            message="high demand",
            status=MlpErrorStatus.SERVICE_UNAVAILABLE,
        )
    )

    assert res.code == "mlp-action.common.service-unavailable"
    assert res.status == SimpleStatusProto.SERVICE_UNAVAILABLE


def test_exception_to_proto():
    res = MlpException.exception_to_proto(MlpException(code="fail", message="total", status=MlpErrorStatus.BAD_REQUEST))

    assert res.code == "fail"
    assert res.message == "total"
    assert res.status == SimpleStatusProto.BAD_REQUEST


def test_exception_to_proto_wrong_types():
    res = MlpException.exception_to_proto(MlpException(code="fail", message="total", status=5))

    assert res.code == "mlp-action.common.internal-error"
    assert res.message == "fail: total"
    assert res.status == SimpleStatusProto.INTERNAL_SERVER_ERROR
