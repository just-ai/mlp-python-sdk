import dataclasses
import json
import os
import tempfile
from datetime import date, datetime, time
from typing import Optional

import numpy as np
import pytest
from box import Box
from pydantic import BaseModel

from mlp_sdk.utils.json_ import JSON, MyJsonEncoder


# Тестовые классы и данные
@dataclasses.dataclass
class _Dataclass:
    name: str
    value: int
    date: Optional[datetime] = None


def test_function() -> None:
    pass


class _PydanticModel(BaseModel):
    name: str
    value: int
    date: Optional[datetime] = None


# Тесты для MyJsonEncoder
def test_datetime_serialization() -> None:
    """Тест сериализации объектов datetime."""
    dt = datetime(2023, 1, 15, 12, 30, 45)
    result = json.dumps(dt, cls=MyJsonEncoder)
    assert result == '"2023-01-15T12:30:45.000"'


def test_date_serialization() -> None:
    """Тест сериализации объектов date."""
    d = date(2023, 1, 15)
    result = json.dumps(d, cls=MyJsonEncoder)
    assert result == '"2023-01-15"'


def test_time_serialization() -> None:
    """Тест сериализации объектов time."""
    t = time(12, 30, 45, 123456)
    result = json.dumps(t, cls=MyJsonEncoder)
    assert result == '"12:30:45.123"'


def test_dataclass_serialization() -> None:
    """Тест сериализации dataclass объектов."""
    data = _Dataclass(name="test", value=42, date=datetime(2023, 1, 15, 12, 30, 45))
    result = json.loads(json.dumps(data, cls=MyJsonEncoder))

    assert result["name"] == "test"
    assert result["value"] == 42
    assert result["date"] == "2023-01-15T12:30:45.000"


def test_callable_serialization() -> None:
    """Тест сериализации callable объектов."""
    result = json.dumps(test_function, cls=MyJsonEncoder)
    assert "test_json_.test_function" in result


def test_numpy_serialization() -> None:
    """Тест сериализации numpy типов."""
    # Тест для numpy.integer
    np_int = np.int32(42)
    result = json.loads(json.dumps(np_int, cls=MyJsonEncoder))
    assert result == 42
    assert isinstance(result, int)

    # Тест для numpy.floating
    np_float = np.float32(3.14)
    result = json.loads(json.dumps(np_float, cls=MyJsonEncoder))
    assert result == pytest.approx(3.14)  # type: ignore
    assert isinstance(result, float)

    # Тест для numpy.ndarray
    np_array = np.array([1, 2, 3, 4, 5])
    result = json.loads(json.dumps(np_array, cls=MyJsonEncoder))
    assert result == [1, 2, 3, 4, 5]
    assert isinstance(result, list)


def test_pydantic_serialization() -> None:
    """Тест сериализации Pydantic моделей."""
    model = _PydanticModel(name="test", value=42, date=datetime(2023, 1, 15, 12, 30, 45))
    result = json.loads(json.dumps(model, cls=MyJsonEncoder))

    assert result["name"] == "test"
    assert result["value"] == 42
    assert result["date"] == "2023-01-15T12:30:45.000"


# Тесты для класса Json
def test_stringify() -> None:
    """Тест метода stringify."""
    data = {"name": "test", "value": 42, "date": datetime(2023, 1, 15, 12, 30, 45)}

    # Тест с pretty=True
    pretty_result = JSON.stringify(data, pretty=True)
    assert "{\n" in pretty_result
    assert "  " in pretty_result  # Проверка отступов

    # Тест с pretty=False
    compact_result = JSON.stringify(data, pretty=False)
    assert "{\n" not in compact_result

    # Проверка содержимого
    parsed = json.loads(pretty_result)
    assert parsed["name"] == "test"
    assert parsed["value"] == 42
    assert parsed["date"] == "2023-01-15T12:30:45.000"


def test_stringify_to_bytes() -> None:
    """Тест метода stringify_to_bytes."""
    data = {"name": "test", "value": 42}
    result = JSON.stringify_to_bytes(data)

    assert isinstance(result, bytes)
    parsed = json.loads(result)
    assert parsed["name"] == "test"
    assert parsed["value"] == 42


def test_parse_dict() -> None:
    """Тест метода parse для словаря без указания класса."""
    json_text = '{"name": "test", "value": 42}'
    result = JSON.parse_(json_text)

    assert isinstance(result, Box)
    assert result.name == "test"  # type: ignore
    assert result.value == 42  # type: ignore


def test_parse_list() -> None:
    """Тест метода parse для списка без указания класса."""
    json_text = "[1, 2, 3, 4, 5]"
    result = JSON.parse_(json_text)

    assert isinstance(result, list)
    assert result == [1, 2, 3, 4, 5]


def test_parse_dataclass() -> None:
    """Тест метода parse с указанием dataclass."""
    json_text = '{"name": "test", "value": 42, "date": "2023-01-15T12:30:45"}'
    result = JSON.parse(json_text, _Dataclass)

    assert isinstance(result, _Dataclass)
    assert result.name == "test"
    assert result.value == 42
    assert isinstance(result.date, datetime)
    assert result.date == datetime(2023, 1, 15, 12, 30, 45)


def test_parse_pydantic() -> None:
    """Тест метода parse с указанием Pydantic модели."""
    json_text = '{"name": "test", "value": 42, "date": "2023-01-15T12:30:45"}'
    result = JSON.parse(json_text, _PydanticModel)

    assert isinstance(result, _PydanticModel)
    assert result.name == "test"
    assert result.value == 42
    assert isinstance(result.date, datetime)
    assert result.date == datetime(2023, 1, 15, 12, 30, 45)


def test_parse_unknown_class() -> None:
    """Тест метода parse с неизвестным типом класса."""
    json_text = '{"name": "test", "value": 42}'

    class UnknownClass:
        pass

    with pytest.raises(Exception, match="Unknown class type"):
        JSON.parse(json_text, UnknownClass)


def test_stringify_base_type() -> None:
    res = JSON.stringify("str", pretty=False)
    assert res == '"str"'


def test_save() -> None:
    """Тест метода save."""
    data = {
        "name": "test", 
    }
    
    # Создаем временный файл для теста
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as temp_file:
        temp_filename = temp_file.name
    
    try:
        # Сохраняем данные в файл
        JSON.save(temp_filename, data)
        
        # Читаем содержимое файла
        with open(temp_filename, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Проверяем содержимое
        parsed = json.loads(content)
        assert parsed["name"] == "test"
    finally:
        # Удаляем временный файл
        if os.path.exists(temp_filename):
            os.unlink(temp_filename)
