import inspect
from abc import ABC, ABCMeta
from typing import Any, Callable, Dict, List, Union, _GenericAlias, get_args

import yaml
from pydantic import BaseModel

from mlp_sdk.allowed_types import BASE_FIELD_TYPES
from mlp_sdk.grpc.mlp_grpc_pb2 import MethodDescriptorProto, ParamDescriptorProto, ServiceDescriptorProto


class TaskMeta(ABCMeta):
    @staticmethod
    def _prettify_name(name: str) -> str:
        if name.startswith("__"):
            name = name[2:]

        if name.endswith("__"):
            name = name[: len(name) - 2]

        return name

    @staticmethod
    def create_function(functions, parameters, defaults, return_annotation) -> Callable:
        def _updated_function(*args, **kwargs):
            for function in functions:
                function.__defaults__ = defaults

            for function in functions[:-1]:
                function(*args, **kwargs)
            return functions[-1](*args, **kwargs)

        wrapped_parameters = [
            inspect.Parameter(
                param, inspect.Parameter.POSITIONAL_OR_KEYWORD, annotation=type_.annotation, default=type_.default
            )
            for param, type_ in parameters.items()
        ]

        _updated_function.__signature__ = inspect.Signature(wrapped_parameters, return_annotation=return_annotation)
        _updated_function.__annotations__ = parameters

        return _updated_function

    def _get_schema(cls) -> Callable:
        def _f() -> Dict[str, Any]:
            schema = {}

            for attr_name in dir(cls):  # we need methods of both class and its parents
                if attr_name.endswith("__METHODS"):
                    for method_name in getattr(cls, attr_name):
                        pretty_method_name = cls._prettify_name(method_name)
                        method_info = inspect.signature(getattr(cls, method_name))

                        schema[pretty_method_name] = {}
                        for param_name, param_value in method_info.parameters.items():
                            if hasattr(param_value.annotation, "schema"):
                                schema[pretty_method_name][param_name] = param_value.annotation.schema()

                            elif param_value.annotation == str:  # noqa: E721
                                schema[pretty_method_name][param_name] = {
                                    "title": param_value.annotation.__name__,
                                    "type": BASE_FIELD_TYPES[param_value.annotation],
                                }
                            elif hasattr(param_value.annotation, "_name") and param_value.annotation._name == "List":
                                inner_value = get_args(param_value.annotation)[0]
                                if hasattr(inner_value, "schema"):
                                    schema[pretty_method_name][param_name] = {
                                        "definitions": {f"{inner_value.__name__}": inner_value.schema()},
                                        "type": BASE_FIELD_TYPES[eval(param_value.annotation._name.lower())],
                                        "items": {"$ref": f"#/definitions/{inner_value.__name__}"},
                                    }

                        if (
                            hasattr(method_info.return_annotation, "_name")
                            and method_info.return_annotation._name == "List"
                        ):
                            inner_value = get_args(method_info.return_annotation)[0]
                            if hasattr(inner_value, "schema"):
                                schema[pretty_method_name]["return"] = {
                                    "definitions": {f"{inner_value.__name__}": inner_value.schema()},
                                    "type": BASE_FIELD_TYPES[eval(method_info.return_annotation._name.lower())],
                                    "items": {"$ref": f"#/definitions/{inner_value.__name__}"},
                                }
                        else:
                            schema[pretty_method_name]["return"] = (
                                method_info.return_annotation.schema()
                                if hasattr(method_info.return_annotation, "schema")
                                else None
                            )

            return schema

        return _f

    def update_methods(cls) -> None:
        for attr_name in dir(cls):  # we need methods of both class and its parents
            if attr_name.endswith("__METHODS"):
                for method_name in getattr(cls, attr_name):
                    pre_method_name = "pre_" + method_name
                    post_method_name = "post_" + method_name

                    main_function = getattr(cls, method_name)
                    signature = inspect.signature(main_function)
                    functions = [main_function]

                    if hasattr(cls, pre_method_name) and not hasattr(cls, post_method_name):
                        pre_function = getattr(cls, pre_method_name)
                        functions = [pre_function, main_function]

                    if not hasattr(cls, pre_method_name) and hasattr(cls, post_method_name):
                        post_function = getattr(cls, post_method_name)
                        functions = [main_function, post_function]

                    if hasattr(cls, pre_method_name) and hasattr(cls, post_method_name):
                        pre_function = getattr(cls, pre_method_name)
                        post_function = getattr(cls, post_method_name)
                        functions = [pre_function, main_function, post_function]

                    setattr(
                        cls,
                        method_name,
                        TaskMeta.create_function(
                            functions,
                            dict(signature.parameters),
                            main_function.__defaults__,
                            signature.return_annotation,
                        ),
                    )

    def __init__(cls, name, bases, dct):
        super(TaskMeta, cls).__init__(name, bases, dct)
        TaskMeta.update_methods(cls)
        setattr(cls, f"_{name}__get_schema", TaskMeta._get_schema(cls))


class ABCTask(ABC, metaclass=TaskMeta):
    # mangled as each mixin must have its own fields
    __METHODS = []
    __IS_LEARNABLE = False

    def _check_config_validness(self, config: Union[BaseModel, List[BaseModel]], stage: str) -> None:
        if config is None:
            return
        gold_schema = getattr(type(self), f"get_{stage}_config_schema")()
        if type(gold_schema) is _GenericAlias:
            outer_value = gold_schema._name
            inner_value = get_args(gold_schema)[0].schema()["title"]

            if type(config) == eval(outer_value.lower()):  # noqa: E721
                for config_el in config:
                    if config_el.schema()["title"] != inner_value:
                        raise RuntimeError("Schemas don't match.")
            else:
                raise RuntimeError("Schemas don't match.")
        elif type(config) is not gold_schema:
            raise RuntimeError("Schemas don't match.")

    @classmethod
    def get_schema(cls) -> Dict[Any, Any]:
        schema = {}
        for method_name in cls.__dict__:  # we need only methods of class
            if method_name.endswith("__get_schema"):
                schema = {**schema, **getattr(cls, method_name)()}

        return schema

    @classmethod
    def get_descriptor(cls) -> ServiceDescriptorProto:
        schema = cls.get_schema()

        def get_return_type(method_schema):
            return_type = "null"
            if method_schema["return"] is None:
                return_type = "null"
            elif method_schema["return"].get("title", ""):
                return_type = method_schema["return"]["title"]
            elif method_schema["return"]["type"] == "array":
                return_type = "array " + method_schema["return"]["items"]["$ref"].split("/")[-1]

            return return_type

        return ServiceDescriptorProto(
            name=cls.__name__,
            fittable=any([getattr(cls, attr_name) for attr_name in dir(cls) if attr_name.endswith("__IS_LEARNABLE")]),  # noqa: C419
            methods={
                method_name: MethodDescriptorProto(
                    input={
                        k: ParamDescriptorProto(
                            type=v["title"] if v["type"] != "array" else "array " + v["items"]["$ref"].split("/")[-1]
                        )
                        for k, v in method_schema.items()
                        if k != "return"
                    },
                    output=ParamDescriptorProto(type=get_return_type(method_schema)),
                )
                for method_name, method_schema in schema.items()
            },
            schemaFiles={"schema": yaml.dump(schema, allow_unicode=True)},
        )

    @property
    def is_batch_predictable(self) -> bool:
        return False

    @property
    def is_learnable(self) -> bool:
        return self.__IS_LEARNABLE
