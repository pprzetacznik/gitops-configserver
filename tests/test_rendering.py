from gitops_mt.config import Config
from gitops_mt.templates_rendering import TemplatesRendering
from pytest import fixture


@fixture
def config():
    config = Config()
    config.CONFIG_DIR = "config"
    config.TARGET_DIR = "target"
    return config


@fixture
def templates_rendering(config):
    yield TemplatesRendering(config)
    print("cleanup")


def test_rendering(templates_rendering):
    templates_rendering.render()
