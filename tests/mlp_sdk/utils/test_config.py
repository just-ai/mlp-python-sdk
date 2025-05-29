import os
import shutil
import tempfile
from dataclasses import dataclass, field

import pytest

from mlp_sdk.utils.config import ConfigException, ConfigLoader, get_config, load_application_config, set_config_dir


@dataclass
class Config1:
    field1: int
    field2: str


@dataclass
class Config2:
    field1: bool
    field2: bool


@dataclass
class Config3:
    field1: float = 3.5


@dataclass
class Config4:
    test1: str = field(metadata={"alias": ["OLD_NAME_FOR_THIS"]})
    inner1: Config1
    inner2: dict = field(default_factory=lambda: {"aa": 5})


class TestConfigLoader:
    def setup_method(self):
        self.config_dir = os.path.join(tempfile.gettempdir(), "test-config-loader")
        shutil.rmtree(self.config_dir, ignore_errors=True)
        os.makedirs(self.config_dir)
        set_config_dir(self.config_dir)

    def config_yml(self, content):
        # Clean content:
        # - remove empty lines
        # - remove common whitespace prefix from other lines
        lines = [line for line in content.split("\n") if line.strip()]
        if not lines:
            return

        # Find common whitespace prefix
        def get_leading_spaces(line):
            return len(line) - len(line.lstrip())

        min_spaces = min(get_leading_spaces(line) for line in lines if line.strip())

        # Remove common prefix
        cleaned_content = "\n".join(line[min_spaces:] if len(line) >= min_spaces else line for line in lines)

        with open(os.path.join(self.config_dir, "config.yml"), "w", encoding="utf-8") as f:
            f.write(cleaned_content.strip())

    def test_simple(self):
        self.config_yml("""
        field1: 5
        field2: hello
        """)

        config = ConfigLoader().load_config(Config1)

        # Assert the values are correctly loaded
        assert config.field1 == 5
        assert config.field2 == "hello"

    def test_no_config(self):
        with pytest.raises(ConfigException):
            ConfigLoader().load_config(Config1)

    def test_bool_from_text(self):
        self.config_yml("""
        field1: "yes"
        field2: 0
        """)

        config = ConfigLoader().load_config(Config2)

        # Assert the values are correctly loaded
        assert config.field1
        assert not config.field2

    def test_no_value(self):
        self.config_yml("""
        field1: yes
        """)

        with pytest.raises(ConfigException):
            ConfigLoader().load_config(Config2)

    def test_conversions(self):
        self.config_yml("""
        field1: "5"
        field2: yes
        """)

        config = ConfigLoader().load_config(Config1)

        assert config.field1 == 5
        assert config.field2 == "True"

    def test_conversion_fails(self):
        self.config_yml("""
        field1: "no-int"
        field2: yes
        """)

        with pytest.raises(ConfigException):
            ConfigLoader().load_config(Config1)

    def test_float(self):
        self.config_yml("""
        field1: 4
        """)

        config = ConfigLoader().load_config(Config3)
        assert config.field1 == 4

    def test_default(self):
        self.config_yml("""
        test: 1
        """)

        config = ConfigLoader().load_config(Config3)
        assert config.field1 == 3.5

    def test_env(self):
        os.environ["FIELD1"] = "5"
        os.environ["FIELD2"] = "True"
        self.config_yml("""
            field1: 1
            field2: no
            """)

        config = ConfigLoader().load_config(Config1)

        assert config.field1 == 5
        assert config.field2 == "True"

    def test_nested_dataclass(self):
        self.config_yml("""
        test1: value1
        inner1:
          field1: 10
          field2: nested_value
        """)

        config = ConfigLoader().load_config(Config4)

        assert config.test1 == "value1"
        assert config.inner1.field1 == 10
        assert config.inner1.field2 == "nested_value"

    def test_nested_dataclass_with_env(self):
        os.environ["INNER1_FIELD2"] = "val from env"
        self.config_yml("""
        test1: value1
        inner1:
          field1: 10
          field2: nested_value
        """)

        config = ConfigLoader().load_config(Config4)

        assert config.inner1.field2 == "val from env"

    def test_alias_loading(self):
        # Test loading via alias from environment variable
        os.environ["OLD_NAME_FOR_THIS"] = "alias_value"
        self.config_yml("""
        inner1:
          field1: 42
          field2: hello_world
        """)

        config = ConfigLoader().load_config(Config4)

        assert config.test1 == "alias_value"  # Should be loaded from env via alias

    def test_default_factory(self):
        self.config_yml("""
        test1: some_value
        inner1:
          field1: 7
          field2: test_string
        # inner2 is not specified, should use default factory
        """)

        config = ConfigLoader().load_config(Config4)

        assert config.inner2["aa"] == 5

    def test_get_config(self):
        import mlp_sdk.utils.config as cc

        cc._base_config = None
        c = get_config()
        assert c.logging.app_name == "mlp_sdk"

    def test_application_config(self):
        self.config_yml("""
        field1: 5
        field2: hello
        """)

        c = load_application_config(Config1, folder=self.config_dir)
        assert c.field1 == 5
