from os.path import join
from gitops_configserver.config import Config
from gitops_configserver.workflow import TemplatesRenderingCommand
from gitops_configserver.utils import read_file, remove_dir_with_content
from pytest import fixture


@fixture
def config():
    config = Config()
    config.CONFIG_DIR = "resources/test_config"
    config.TARGET_DIR = "target_test_configserver"
    return config


@fixture
def templates_rendering_command(config):
    yield TemplatesRenderingCommand(config)
    # remove_dir_with_content(config.TARGET_DIR)


def test_rendering(templates_rendering_command, config):
    templates_rendering_command.execute()
    content = read_file(
        join(
            config.TARGET_DIR,
            "tenant1",
            "config1-ubuntu-22.04-10-python3.7-prod.yml",
        )
    )
    assert (
        content
        == """- my_config:
  - var1: aaa1.default
  - var2: bbb1.default
  - var3: ccc1.default
  - lll: |
    - abc: 1
      def: 2
      ghi: 3
    - mmm: 4"""
    )
