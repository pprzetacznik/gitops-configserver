from os.path import join
from gitops_configserver.config import Config
from gitops_configserver.templates_rendering import TemplatesRendering
from gitops_configserver.utils import read_file, remove_dir_with_content
from pytest import fixture


@fixture
def config():
    config = Config()
    config.CONFIG_DIR = "resources/test_config"
    config.TARGET_DIR = "target_test_configserver"
    return config


@fixture
def templates_rendering(config):
    yield TemplatesRendering(config)
    # remove_dir_with_content(config.TARGET_DIR)


def test_rendering(templates_rendering, config):
    templates_rendering.render()
    content = read_file(join(config.TARGET_DIR, "tenant1", "config1.yml"))
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
