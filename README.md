## Usage:

```
sh build.sh <NEXUS_USERNAME> <NEXUS_PASSWORD> <BUILD_NUMBER> <BRANCH_NAME> <SEND_TO_NEXUS>
```

- `<NEXUS_USERNAME>` and `<NEXUS_PASSWORD>` is your IPA credentials.
- `<BUILD_NUMBER>` for development version you can use any value, but if you want to push your package to nexsus please 
check last version [here](https://nexus.just-ai.com/service/rest/repository/browse/pypi-hosted/mlp-sdk/)
- `<BRANCH_NAME>` your development branch name
- `<SEND_TO_NEXUS>` by default set this value to 0. If you want to push your package set this to 1.

## Dev guide:

1. `git clone`
2. `cd mlp-python-sdk`
3. `export mlp_sdk_home=$PWD`
4. Run `pip install -e .`
5. Run tests
6. Library is ready to work with

``` python
   from mlp_sdk.types import TextsCollection
   
   def TextProcessor():
       my_texts = TextsCollection()
       my_texts.extend(["text1", "text2"])
       ...
```

6. Run tests
7. In case of using inheritance when defining source (pydantic) classes with replacement of one or more base-fields
    types you should check that new types are inherited from corresponding old types

### Troubleshooting
1. If you have problems like `Failed to establish a new connection`, try to add `--network=host` 
to all docker commands in `build.sh`

### Allowed fields of custom source types:

- Basic python types: `int`, `float`, `str`, `bool`
- Enumerations:

``` python
import enum
from pydantic import BaseModel


class TokenPosTag(enum.Enum):
    UNKNOWN = 'UNKNOWN'


class MyType(BaseModel):
    pos: TokenPosTag
```

- Another source type:

``` python
from pydantic import BaseModel


class TextType(BaseModel):
    text: str


class TextWithExtra(BaseModel):
    text_field: TextType
    extra_field: str

```

- Any of above with `List` generic type if you want your field to be repeated:

``` python
import enum
from typing import List
from pydantic import BaseModel


class TokenPosTag(enum.Enum):
    UNKNOWN = 'UNKNOWN'


class MyType(BaseModel):
    pos_tags: List[TokenPosTag]
```

### How correctly describe init_config_schema and predict_config_schema.

1. Return only **pydantic** `BaseModel` type or your own type inherited from `BaseModel`.
   
   - If your schema has no parameters, you can simply return `BaseModel`

     ``` python
       def init_config_schema(self) -> Type[BaseModel]:
           return BaseModel
       ...
       def predict_config_schema(self) -> Type[BaseModel]:
           return BaseModel
     ```
    
   - For describing your config schema define complex types as classes inherited from `BaseModel` and fill your config
     schema by them.

     ``` python
        class DucklingContext(BaseModel):
            locale: str

        class ParamsType(BaseModel):
            duckling_context: DucklingContext
   
        class Entity(BaseModel):
            name: str version = "v1"
    
        class SystemEntities(BaseModel):
            entities: List[Entity]
    
        class NerPredictConfigSchema(BaseModel):
            lang: str
            engines: List[str]
            params: ParamsType
            systemEntities: SystemEntities
     ```
   
     and with predict config example above your `predict_config_schema` will look like this:
   
     ```python  
       def predict_config_schema(self) -> Type[BaseModel]:
           return NerPredictConfigSchema
     ```

### How to use storages

- Import one of implemented storage from `mlp_sdk.storage` (S3Storage or LocalStorage)
- Create config file and pass it in task through Dockerfile variable (also you can put config data in existing container config file)
- Config should contain the `storage_type` param with `s3` or `local` value
- Also, config should contain all the necessary key-value param pairs for chosen storage (see `__init__` params in corresponding files in `storage` module)
- In the task you can check the given storage type with the following statement:

```python
if container_config['storage_type'] == LocalStorage.name():
    pass
```

Here's an example of config data for `LocalStorage`:
 
```buildoutcfg
storage_type: local
models_dir: my-nlp-models
```

__Attention__: the test case for S3 storage is created for Bitbacket CI environment and will fail during local run, it's normal (as you can't provide a necessary config for it).  

## Examples of usage

See `./examples`
