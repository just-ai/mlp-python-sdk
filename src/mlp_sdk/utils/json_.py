import dataclasses
import json
from datetime import date, datetime, time
from typing import Any, Final, Type, TypeVar, cast

import dacite
from box import Box
from dacite import from_dict
from google.protobuf.json_format import MessageToJson
from google.protobuf.message import Message

try:
    import numpy as np
except ImportError:  # pragma: no cover
    np = None  # type: ignore

try:
    from pydantic import BaseModel
except ImportError:  # pragma: no cover
    BaseModel = None  # type: ignore


class MyJsonEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, datetime):
            return o.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
        if isinstance(o, date):
            return o.strftime("%Y-%m-%d")
        if isinstance(o, time):
            return o.strftime("%H:%M:%S.%f")[:-3]
        if dataclasses.is_dataclass(o) and not isinstance(o, type):
            return dataclasses.asdict(o)
        if callable(o):
            return o.__module__ + "." + o.__name__

        if np is not None:
            if isinstance(o, np.integer):
                return int(cast(int, o))
            if isinstance(o, np.floating):
                return float(cast(float, o))
            if isinstance(o, np.ndarray):
                return o.tolist()

        if BaseModel is not None:
            if isinstance(o, BaseModel):
                return o.model_dump()

        if isinstance(o, Message):
            return MessageToJson(o)

        raise Exception("Unexpected flow")  # pragma: no cover
        # other possible solution: return super(MyJsonEncoder, self).default(o)


T = TypeVar("T")


class Json:
    def __init__(self):
        self.dacite_config = dacite.Config(type_hooks={datetime: lambda s: datetime.fromisoformat(s)})

    def stringify(self, obj: Any, pretty: bool = True) -> str:
        if pretty:
            indent = 2
        else:
            indent = None
        return json.dumps(obj, ensure_ascii=False, indent=indent, cls=MyJsonEncoder)

    def stringify_to_bytes(self, obj: Any, pretty: bool = False) -> bytes:
        return self.stringify(obj, pretty).encode("utf-8")

    def parse(self, json_text: str, clazz: Type[T]) -> T:
        if dataclasses.is_dataclass(clazz):
            return from_dict(clazz, json.loads(json_text), self.dacite_config)
        if BaseModel is not None:
            if issubclass(clazz, BaseModel):
                return clazz.model_validate_json(json_text)
        raise Exception("Unknown class type")

    def parse_(self, json_text: str) -> Any:
        js = json.loads(json_text)
        if type(js) is dict:
            return Box(js)
        else:
            return js

    def save(self, filename: str, data: Any, indent: int = 2) -> None:
        with open(filename, "w", encoding="utf-8") as f:
            content = json.dumps(data, ensure_ascii=False, indent=indent, cls=MyJsonEncoder)
            f.write(content)


JSON: Final[Json] = Json()
