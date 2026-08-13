import threading
import time

import pytest

from mlp_sdk.mlp_connector import client as client_module
from mlp_sdk.mlp_connector.client import MlpGrpcClient, MlpGrpcClientException
from mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2 import ClientResponseProto, PayloadProto, PredictResponseProto

CHANNEL_CLOSED_MESSAGE = "Cannot invoke RPC: Channel closed!"


class FakeChannel:
    """Канал, который умеет только то, что от него нужно клиенту: закрываться и помнить об этом."""

    def __init__(self, name: str):
        self.name = name
        self.closed = False

    def close(self) -> None:
        self.closed = True

    def __repr__(self) -> str:
        return f"FakeChannel({self.name}, closed={self.closed})"


class FakeStub:
    """Стаб, который помнит свой канал и падает на вызовах, если канал уже закрыт (как cygrpc)."""

    def __init__(self, channel: FakeChannel):
        self.channel = channel

    def healthCheck(self, request, timeout=None):  # noqa: N802 - имя метода задано grpc-контрактом
        self.__check_channel()

    def processResponseStream(self, request):  # noqa: N802 - имя метода задано grpc-контрактом
        self.__check_channel()
        return iter([predict_response()])

    def __check_channel(self) -> None:
        if self.channel.closed:
            raise ValueError(CHANNEL_CLOSED_MESSAGE)


def predict_response() -> ClientResponseProto:
    return ClientResponseProto(predict=PredictResponseProto(data=PayloadProto(json="{}")))


@pytest.fixture
def channels(monkeypatch) -> list[FakeChannel]:
    """Подменяет создание канала и стаба, возвращает список созданных каналов в порядке создания."""
    created: list[FakeChannel] = []

    def fake_open_grpc_channel(host_port: str, secure: bool) -> FakeChannel:
        channel = FakeChannel(f"channel-{len(created)}")
        created.append(channel)
        return channel

    monkeypatch.setattr(MlpGrpcClient, "open_grpc_channel", staticmethod(fake_open_grpc_channel))
    monkeypatch.setattr(client_module, "GateStub", FakeStub)
    return created


def make_client() -> MlpGrpcClient:
    return MlpGrpcClient(url="grpc://host:9999", token="test-token")


class TestMlpGrpcClientConnect:
    def test_concurrent_connect_keeps_stub_on_live_channel(self, channels, monkeypatch):
        """Два одновременных reconnect не должны оставить stub на канале, который закрыл другой поток."""
        client = make_client()

        first_stub_ready = threading.Event()
        second_finished = threading.Event()

        def gating_stub(channel):
            # второй поток создаёт свой стаб только после того, как первый уже завёл свой
            if threading.current_thread().name == "second":
                first_stub_ready.wait(timeout=1)
            return FakeStub(channel)

        def sync_healthcheck(self, request, timeout=None):
            if threading.current_thread().name == "first":
                first_stub_ready.set()
                # первый поток заканчивает connect последним — так стаб и канал расходятся
                second_finished.wait(timeout=1)

        monkeypatch.setattr(client_module, "GateStub", gating_stub)
        monkeypatch.setattr(FakeStub, "healthCheck", sync_healthcheck)

        def reconnect() -> None:
            client.connect()
            if threading.current_thread().name == "second":
                second_finished.set()

        threads = [threading.Thread(target=reconnect, name=name) for name in ("first", "second")]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join(timeout=10)

        assert client.stub is not None
        assert client.stub.channel is client.channel, "stub привязан не к тому каналу, который клиент считает текущим"
        assert not client.channel.closed, "stub остался на закрытом канале"
        # каналы, которые клиент больше не использует, должны быть закрыты
        assert [channel for channel in channels if not channel.closed] == [client.channel]

    def test_failed_health_check_keeps_previous_connection(self, channels, monkeypatch):
        """Неудачный healthCheck не меняет состояние клиента и закрывает свежесозданный канал."""
        client = make_client()
        working_channel = client.channel
        working_stub = client.stub

        def failing_healthcheck(self, request, timeout=None):
            raise ValueError("healthCheck failed")

        monkeypatch.setattr(FakeStub, "healthCheck", failing_healthcheck)

        client.connect()

        assert client.stub is working_stub
        assert client.channel is working_channel
        assert not working_channel.closed
        assert len(channels) == 2
        assert channels[1].closed, "канал неудачного connect остался открытым"

    def test_health_check_is_called_with_timeout(self, channels, monkeypatch):
        """healthCheck идёт под connect_lock, поэтому у него должен быть дедлайн."""
        timeouts: list[object] = []

        def recording_healthcheck(self, request, timeout=None):
            timeouts.append(timeout)

        monkeypatch.setattr(FakeStub, "healthCheck", recording_healthcheck)

        make_client()

        assert timeouts, "healthCheck не вызывался"
        assert all(isinstance(timeout, (int, float)) and timeout > 0 for timeout in timeouts), f"healthCheck вызван без таймаута: {timeouts}"


class TestMlpGrpcClientRequestRetry:
    def test_closed_channel_value_error_triggers_reconnect(self, channels, monkeypatch):
        """ValueError закрытого канала лечится переподключением и повтором запроса, а не падает наружу."""
        client = make_client()
        # имитируем гонку: канал, на котором висит стаб, закрыт кем-то ещё
        client.channel.close()

        result = client.predict("account/model", {})

        assert result == {}
        assert client.stub is not None
        assert not client.stub.channel.closed
        assert len(channels) == 2

    def test_other_value_error_is_not_swallowed(self, channels, monkeypatch):
        """Посторонний ValueError не должен превращаться в бесконечный retry."""
        client = make_client()

        def broken_stream(self, request):
            raise ValueError("something else")

        monkeypatch.setattr(FakeStub, "processResponseStream", broken_stream)

        with pytest.raises(ValueError, match="something else"):
            client.predict("account/model", {})

    def test_permanently_closed_channel_ends_with_client_exception(self, channels, monkeypatch):
        """Если переподключение не помогает, клиент отдаёт свою ошибку, а не голый ValueError."""
        client = make_client()

        def always_closed_stream(self, request):
            raise ValueError(CHANNEL_CLOSED_MESSAGE)

        monkeypatch.setattr(FakeStub, "processResponseStream", always_closed_stream)
        monkeypatch.setattr(client_module.config.sdk, "request_retry_timeout_seconds", 1)
        monkeypatch.setattr(client_module.config.sdk, "request_retry_backoff_seconds", 0.01)

        with pytest.raises(MlpGrpcClientException):
            client.predict("account/model", {})


class TestMlpGrpcClientStartWithDeadGate:
    """Клиент, стартовавший при недоступном gate, обязан переподключиться сам — без stub он не бесполезен навсегда."""

    @pytest.fixture
    def fast_retry(self, monkeypatch):
        monkeypatch.setattr(client_module.config.sdk, "request_retry_timeout_seconds", 1)
        monkeypatch.setattr(client_module.config.sdk, "request_retry_backoff_seconds", 0.01)

    def test_client_recovers_when_gate_comes_back(self, channels, monkeypatch, fast_retry):
        """Первый connect() упал, клиент создался; когда gate ожил — следующий запрос реконнектится и проходит."""
        gate_is_down = {"value": True}

        def flaky_healthcheck(self, request, timeout=None):
            if gate_is_down["value"]:
                raise ValueError("gate is down")

        monkeypatch.setattr(FakeStub, "healthCheck", flaky_healthcheck)

        client = make_client()
        assert client.stub is None, "провальный healthCheck не должен оставлять stub"
        assert client.channel is None

        gate_is_down["value"] = False

        result = client.predict("account/model", {})

        assert result == {}
        assert client.stub is not None, "клиент не переподключился после того, как gate ожил"
        assert client.stub.channel is client.channel
        assert not client.channel.closed

    def test_dead_gate_ends_with_unavailable_and_does_not_hang(self, channels, monkeypatch, fast_retry):
        """Gate так и не ожил: после дедлайна наружу уходит MlpGrpcClientException UNAVAILABLE, процесс не висит."""

        def failing_healthcheck(self, request, timeout=None):
            raise ValueError("gate is down")

        monkeypatch.setattr(FakeStub, "healthCheck", failing_healthcheck)

        client = make_client()
        assert client.stub is None

        started = time.time()
        with pytest.raises(MlpGrpcClientException) as error:
            client.predict("account/model", {})
        elapsed = time.time() - started

        assert error.value.error_code == "UNAVAILABLE"
        assert "Cannot connect" in error.value.error_message
        assert elapsed < 10, f"retry-цикл должен закончиться по дедлайну, а он занял {elapsed:.1f}s"
        # каждый провальный connect закрывает за собой непроверенный канал
        assert channels, "каналы вообще не создавались"
        assert all(channel.closed for channel in channels)
