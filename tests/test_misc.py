import pytest

from mlp_sdk.utils.misc import get_one_of, parse_grpc_url, required


class TestParseGrpcUrl:
    def test_parse_http_url_without_port(self):
        # Тестирование HTTP URL без указания порта
        url = "http://example.com"
        host_port, secure = parse_grpc_url(url)
        assert host_port == "example.com:80"
        assert not secure

    def test_parse_https_url_without_port(self):
        # Тестирование HTTPS URL без указания порта
        url = "https://example.com"
        host_port, secure = parse_grpc_url(url)
        assert host_port == "example.com:443"
        assert secure

    def test_parse_http_url_with_port(self):
        # Тестирование HTTP URL с указанием порта
        url = "http://example.com:8080"
        host_port, secure = parse_grpc_url(url)
        assert host_port == "example.com:8080"
        assert not secure

    def test_parse_https_url_with_port(self):
        # Тестирование HTTPS URL с указанием порта
        url = "https://example.com:8443"
        host_port, secure = parse_grpc_url(url)
        assert host_port == "example.com:8443"
        assert secure


class TestRequired:
    def test_required_with_value(self):
        # Тестирование с непустым значением
        value = "test"
        result = required(value)
        assert result == value

    def test_required_with_none_default_message(self):
        # Тестирование с None и стандартным сообщением об ошибке
        with pytest.raises(Exception) as excinfo:
            required(None)
        assert str(excinfo.value) == "Value is required"

    def test_required_with_none_custom_message(self):
        # Тестирование с None и пользовательским сообщением об ошибке
        custom_message = "Custom error message"
        with pytest.raises(Exception) as excinfo:
            required(None, custom_message)
        assert str(excinfo.value) == custom_message


class TestGetOneOf:
    def test_get_one_of_first_not_none(self):
        # Тестирование, когда первый аргумент не None
        result = get_one_of("first", "second", None)
        assert result == "first"

    def test_get_one_of_second_not_none(self):
        # Тестирование, когда второй аргумент не None
        result = get_one_of(None, "second", None)
        assert result == "second"

    def test_get_one_of_last_not_none(self):
        # Тестирование, когда последний аргумент не None
        result = get_one_of(None, None, "last")
        assert result == "last"

    def test_get_one_of_all_none_default_message(self):
        # Тестирование, когда все аргументы None и стандартное сообщение об ошибке
        with pytest.raises(Exception) as excinfo:
            get_one_of(None, None, None)
        assert str(excinfo.value) == "No value for required field"

    def test_get_one_of_all_none_custom_message(self):
        # Тестирование, когда все аргументы None и пользовательское сообщение об ошибке
        custom_message = "Custom error message"
        with pytest.raises(Exception) as excinfo:
            get_one_of(None, None, None, error_message=custom_message)
        assert str(excinfo.value) == custom_message

    def test_get_one_of_with_different_types(self):
        # Тестирование с аргументами разных типов
        result = get_one_of(None, 42, None)
        assert result == 42

        result = get_one_of(None, None, [1, 2, 3])
        assert result == [1, 2, 3]
