import enum
import typing
from inspect import signature

import pydantic

from mlp_sdk.utilities.schemes_handling import get_parent_classes

from mlp_sdk.allowed_types import BASE_FIELD_TYPES


def can_type_be_replaced(reference_type: type, candidate_type: type) -> bool:
    if reference_type is candidate_type:
        return True

    parents = get_parent_classes(candidate_type)
    if reference_type not in parents:
        return False

    candidate_type_fields = candidate_type.__dict__['__fields__']
    reference_type_fields = reference_type.__dict__['__fields__']

    for field_name, field in candidate_type_fields.items():
        candidate_field_type = field.outer_type_

        # we are not interested in new fields
        if field_name not in reference_type_fields:
            continue

        reference_field_type = reference_type_fields[field_name].outer_type_

        if candidate_field_type in BASE_FIELD_TYPES or issubclass(type(candidate_field_type), enum.EnumMeta):
            if reference_field_type is not candidate_field_type:
                return False

        elif issubclass(type(candidate_field_type), pydantic.main.ModelMetaclass):
            if not can_type_be_replaced(reference_field_type, candidate_field_type):
                return False

        elif issubclass(type(candidate_field_type), typing._GenericAlias):
            if not issubclass(type(reference_field_type), typing._GenericAlias):
                return False

            candidate_generic_type = candidate_field_type.__dict__['__origin__']
            reference_generic_type = reference_field_type.__dict__['__origin__']

            if reference_generic_type is not candidate_generic_type:
                return False

            candidate_inner_type = candidate_field_type.__dict__['__args__'][0]
            reference_inner_type = reference_field_type.__dict__['__args__'][0]

            if candidate_inner_type in BASE_FIELD_TYPES or issubclass(type(candidate_inner_type), enum.EnumMeta):
                if candidate_inner_type is not reference_inner_type:
                    return False

            elif issubclass(type(candidate_inner_type), pydantic.main.ModelMetaclass):
                if not can_type_be_replaced(reference_inner_type, candidate_inner_type):
                    return False
            else:
                return False
        else:
            return False

    return True


def is_allowed_input_type(task: type, method: str, argument: str, type_: type) -> bool:
    data_annotation_type = signature(getattr(task, method)).parameters[argument].annotation

    if type(data_annotation_type) is typing._GenericAlias:
        data_annotation_type = typing.get_args(data_annotation_type)[0]

    return can_type_be_replaced(type_, data_annotation_type)
