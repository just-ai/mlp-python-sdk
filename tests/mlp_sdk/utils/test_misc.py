import pytest

from mlp_sdk.utils.misc import get_one_of, parse_grpc_url, remove_null_fields, required


class TestParseGrpcUrl:
    def test_parse_url_without_protocol(self):
        # Тестирование URL без указания протокола
        url = "localhost:50051"
        host_port, secure = parse_grpc_url(url)
        assert host_port == "localhost:50051"
        assert secure

    def test_parse_url_with_invalid_hostname(self):
        # Тестирование URL, в котором отсутствует хост
        url = "http://"
        with pytest.raises(Exception) as excinfo:
            parse_grpc_url(url)
        assert "Invalid url" in str(excinfo.value)

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


class TestRemoveNullFields:
    def test_remove_null_fields_simple_dict(self):
        # Тестирование с простым словарем
        input_dict = {"a": 1, "b": None, "c": "test"}
        expected = {"a": 1, "c": "test"}
        result = remove_null_fields(input_dict)
        assert result == expected

    def test_remove_null_fields_nested_dict(self):
        # Тестирование с вложенным словарем
        input_dict = {"a": 1, "b": None, "c": {"d": "test", "e": None, "f": 42}}
        expected = {"a": 1, "c": {"d": "test", "f": 42}}
        result = remove_null_fields(input_dict)
        assert result == expected

    def test_remove_null_fields_with_list(self):
        # Тестирование со списком
        input_dict = {"a": 1, "b": None, "c": [{"d": "test", "e": None}, {"f": None, "g": 42}, None, "string"]}
        expected = {"a": 1, "c": [{"d": "test"}, {"g": 42}, None, "string"]}
        result = remove_null_fields(input_dict)
        assert result == expected

    def test_remove_null_fields_empty_dict(self):
        # Тестирование с пустым словарем
        input_dict = {}
        expected = {}
        result = remove_null_fields(input_dict)
        assert result == expected

    def test_remove_null_fields_all_none(self):
        # Тестирование со словарем, где все значения None
        input_dict = {"a": None, "b": None, "c": None}
        expected = {}
        result = remove_null_fields(input_dict)
        assert result == expected

    def test_remove_null_fields_non_dict(self):
        # Тестирование с не-словарем
        input_value = "not a dict"
        result = remove_null_fields(input_value)
        assert result == input_value

        input_value = 42
        result = remove_null_fields(input_value)
        assert result == input_value

        input_value = None
        result = remove_null_fields(input_value)
        assert result == input_value
