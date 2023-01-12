from mlp_sdk.utilities.schemes_handling import get_parent_classes
from mlp_sdk.types import (TokensErrorTest,
                           InflectorConformerTextsCollectionTest,
                           ConformerTextsCollection,
                           InflectorTextsCollection,
                           TokenizedTextsCollection,
                           TokenizedTextsCollectionTest,
                           TokenizedTextsCollectionWithErrorTest,
                           TextsCollection,
                           TokensTest)
from mlp_sdk.abstract.task_utils import can_type_be_replaced


def test_get_parents():
    based_on = set(get_parent_classes(InflectorConformerTextsCollectionTest))
    assert based_on == {ConformerTextsCollection,
                        InflectorTextsCollection,
                        TextsCollection}


def test_inheritance_hierarchy():
    assert can_type_be_replaced(TokenizedTextsCollection,
                                TokenizedTextsCollectionTest)


def test_inheritance_hierarchy_incorrect_1():
    assert not can_type_be_replaced(TokenizedTextsCollection,
                                    TokenizedTextsCollectionWithErrorTest)


def test_inheritance_hierarchy_incorrect_2():
    assert not can_type_be_replaced(TokensTest, TokensErrorTest)
