import inspect

from pydantic.main import BaseModel

from mlp_sdk.abstract.abc_task import TaskMeta
from mlp_sdk.abstract import Task


class TaskWithPreOnly(Task):
    __METHODS = ["main"]

    def pre_main(self, config: BaseModel, str_arg: str, int_arg: int):
        print(f"Pre function with str_arg: {str_arg} and int_arg: {int_arg}")

    def main(self, config: BaseModel, str_arg: str = 'a', int_arg: int = 0):
        print(f"Main function with str_arg: {str_arg} and int_arg: {int_arg}")

    def predict(self, data: BaseModel, config: BaseModel) -> BaseModel:
        pass


class TaskWithPostOnly(Task):
    __METHODS = ["main"]

    def post_main(self, config: BaseModel, str_arg: str, int_arg: int):
        print(f"Post function with str_arg: {str_arg} and int_arg: {int_arg}")

    def main(self, config: BaseModel, str_arg: str = 'a', int_arg: int = 0):
        print(f"Main function with str_arg: {str_arg} and int_arg: {int_arg}")

    def predict(self, data: BaseModel, config: BaseModel) -> BaseModel:
        pass


class TaskWithPreAndPost(Task):
    __METHODS = ["main"]

    def pre_main(self, config: BaseModel, str_arg: str, int_arg: int):
        print(f"Pre function with str_arg: {str_arg} and int_arg: {int_arg}")

    def post_main(self, config: BaseModel, str_arg: str, int_arg: int):
        print(f"Post function with str_arg: {str_arg} and int_arg: {int_arg}")

    def main(self, config: BaseModel, str_arg: str = 'a', int_arg: int = 0):
        print(f"Main function with str_arg: {str_arg} and int_arg: {int_arg}")

    def predict(self, data: BaseModel, config: BaseModel) -> BaseModel:
        pass


class TaskWithoutPreAndPost(Task):
    __METHODS = ["main"]

    def main(self, config: BaseModel, str_arg: str = 'a', int_arg: int = 0):
        print(f"Main function with str_arg: {str_arg} and int_arg: {int_arg}")

    def predict(self, data: BaseModel, config: BaseModel) -> BaseModel:
        pass


class SimpleConfig(BaseModel):
    name: str


def pre_function(config: BaseModel, str_arg: str, int_arg: int):
    print("Pre function")


def main_function(config: BaseModel, str_arg: str = '', int_arg: int = 0):
    print("Main function")


def post_function(config: BaseModel, str_arg: str, int_arg: int):
    print("Post function")


def test_create_function():
    signature_main = inspect.signature(main_function)

    modified_func_with_pre = TaskMeta.create_function(
        [pre_function, main_function],
        dict(signature_main.parameters),
        main_function.__defaults__,
        signature_main.return_annotation,
    )

    signature_with_pre = inspect.signature(modified_func_with_pre)
    assert signature_main.parameters == signature_with_pre.parameters
    assert signature_main.return_annotation == signature_with_pre.return_annotation

    modified_func_with_post = TaskMeta.create_function(
        [main_function, post_function],
        dict(signature_main.parameters),
        main_function.__defaults__,
        signature_main.return_annotation,
    )

    signature_with_post = inspect.signature(modified_func_with_post)
    assert signature_main.parameters == signature_with_post.parameters
    assert signature_main.return_annotation == signature_with_post.return_annotation

    modified_func_with_pre_post = TaskMeta.create_function(
        [pre_function, main_function, post_function],
        dict(signature_main.parameters),
        main_function.__defaults__,
        signature_main.return_annotation,
    )

    signature_with_pre_post = inspect.signature(modified_func_with_post)
    assert signature_main.parameters == signature_with_pre_post.parameters
    assert signature_main.return_annotation == signature_with_pre_post.return_annotation

    print()
    modified_func_with_pre(config=SimpleConfig(name="pre"))
    print()
    modified_func_with_post(config=SimpleConfig(name="post"))
    print()
    modified_func_with_pre_post(config=SimpleConfig(name="post"))


def test_task_with_pre_and_post():
    task_with_pre_only = TaskWithPreOnly(BaseModel())
    print()
    task_with_pre_only.main(BaseModel())

    task_with_post_only = TaskWithPostOnly(BaseModel())
    print()
    task_with_post_only.main(BaseModel())

    task_with_pre_and_post = TaskWithPreAndPost(BaseModel())
    print()
    task_with_pre_and_post.main(BaseModel())

    task_with_main_only = TaskWithoutPreAndPost(BaseModel())
    print()
    task_with_main_only.main(BaseModel())
