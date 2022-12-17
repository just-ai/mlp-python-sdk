from abc import ABC, ABCMeta
from typing import Dict, Any, Callable, Union, List, _GenericAlias, get_args
from inspect import signature

from pydantic import BaseModel

from caila_sdk.grpc.mpl_grpc_pb2 import ActionDescriptorProto, MethodDescriptorProto, ParamDescriptorProto
from caila_sdk.allowed_types import BASE_FIELD_TYPES


class TaskMeta(ABCMeta):
    @staticmethod
    def _prettify_name(name: str) -> str:
        if name.startswith('__'):
            name = name[2:]

        if name.startswith('_'):
            name = name[1:]

        if name.endswith('__'):
            name = name[: len(name) - 2]

        if name.endswith('_'):
            name = name[: len(name) - 1]

        return name

    def _get_schema(cls) -> Callable:
        def _f() -> Dict[str, Any]:
            schema = {}

            for attr_name in dir(cls):  # we need methods of both class and its parents
                if attr_name.endswith('__METHODS'):
                    for method_name in getattr(cls, attr_name):

                        pretty_method_name = cls._prettify_name(method_name)
                        method_info = signature(getattr(cls, method_name))

                        schema[pretty_method_name] = {}
                        for param_name, param_value in method_info.parameters.items():
                            if hasattr(param_value.annotation, 'schema'):
                                schema[pretty_method_name][param_name] = param_value.annotation.schema()

                            elif param_value.annotation == str:
                                schema[pretty_method_name][param_name] = {
                                    'title': param_value.annotation.__name__,
                                    'type': BASE_FIELD_TYPES[param_value.annotation],
                                }
                            elif hasattr(param_value.annotation, "_name") and param_value.annotation._name == "List":
                                inner_value = get_args(param_value.annotation)[0]
                                if hasattr(inner_value, 'schema'):
                                    schema[pretty_method_name][param_name] = {
                                        "definitions": {
                                            f"{inner_value.__name__}": inner_value.schema()
                                        },
                                        "type": BASE_FIELD_TYPES[eval(param_value.annotation._name.lower())],
                                        "items": {"$ref": f"#/definitions/{inner_value.__name__}"}
                                    }

                        if hasattr(method_info.return_annotation,
                                   "_name") and method_info.return_annotation._name == "List":
                            inner_value = get_args(method_info.return_annotation)[0]
                            if hasattr(inner_value, 'schema'):
                                schema[pretty_method_name]['return'] = {
                                    "definitions": {
                                        f"{inner_value.__name__}": inner_value.schema()
                                    },
                                    "type": BASE_FIELD_TYPES[eval(method_info.return_annotation._name.lower())],
                                    "items": {"$ref": f"#/definitions/{inner_value.__name__}"}
                                }
                        else:
                            schema[pretty_method_name]['return'] = (
                                method_info.return_annotation.schema()
                                if hasattr(method_info.return_annotation, 'schema') else None
                            )

            return schema

        return _f

    def __init__(cls, name, bases, dct):
        super(TaskMeta, cls).__init__(name, bases, dct)
        setattr(cls, f'_{name}__get_schema', TaskMeta._get_schema(cls))


class ABCTask(ABC, metaclass=TaskMeta):
    # mangled as each mixin must have its own fields
    __METHODS = []
    __IS_LEARNABLE = False

    def _check_config_validness(self, config: Union[BaseModel, List[BaseModel]], stage: str) -> None:
        gold_schema = getattr(type(self), f"get_{stage}_config_schema")()
        if type(gold_schema) is _GenericAlias:
            outer_value = gold_schema._name
            inner_value = get_args(gold_schema)[0].schema()["title"]

            if type(config) == eval(outer_value.lower()):
                for config_el in config:
                    if config_el.schema()["title"] != inner_value:
                        raise RuntimeError("Schemas don't match.")
            else:
                raise RuntimeError("Schemas don't match.")
        elif not (type(config) is gold_schema):
            raise RuntimeError("Schemas don't match.")

    @classmethod
    def get_schema(cls) -> Dict[Any, Any]:
        schema = {}
        for method_name in cls.__dict__:  # we need only methods of class
            if method_name.endswith('__get_schema'):
                schema = {**schema, **getattr(cls, method_name)()}

        return schema

    @classmethod
    def get_descriptor(cls) -> ActionDescriptorProto:
        schema = cls.get_schema()

        def get_return_type(method_schema):
            return_type = 'null'
            if method_schema["return"] is None:
                return_type = 'null'
            elif method_schema["return"].get("title", ""):
                return_type = method_schema['return']['title']
            elif method_schema["return"]["type"] == "array":
                return_type = "array " + method_schema["return"]["items"]["$ref"].split("/")[-1]

            return return_type

        return ActionDescriptorProto(
            name=cls.__name__,
            fittable=any([getattr(cls, attr_name) for attr_name in dir(cls) if attr_name.endswith('__IS_LEARNABLE')]),
            methods={
                method_name: MethodDescriptorProto(
                    input={
                        k: ParamDescriptorProto(
                            type=v['title'] if v["type"] != "array" else "array " + v["items"]["$ref"].split("/")[-1])
                        for k, v in method_schema.items() if k != 'return'
                    },
                    output=ParamDescriptorProto(type=get_return_type(method_schema))
                )
                for method_name, method_schema in schema.items()
            }
        )

    @property
    def is_batch_predictable(self) -> bool:
        return False
