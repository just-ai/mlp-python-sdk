from mlp_sdk.abstract.services import MlpErrorStatus, MlpException
from mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2 import SimpleStatusProto


def test_from_proto():
    # Test conversion from proto with OK status
    ss = SimpleStatusProto.INTERNAL_SERVER_ERROR
    assert MlpErrorStatus.from_proto(ss) == MlpErrorStatus.INTERNAL_SERVER_ERROR


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
