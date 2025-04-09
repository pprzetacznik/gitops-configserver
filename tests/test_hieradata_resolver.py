from pytest import fixture
from gitops_configserver.hieradata_resolver import HieradataResolver
from gitops_configserver.config import Config


@fixture
def config():
    config = Config()
    config.CONFIG_DIR = "resources/test_config"
    return config


def test_hieradata(config):
    assert HieradataResolver(config).render(
        "tenant1", {"environment": "prod", "node": "node1"}
    ) == {
        "aaa": "aaa1.prod",
        "bbb": "bbb1.prod",
        "ccc": "ccc1.default",
        "ddd": [{"abc": 1, "def": 2, "ghi": 3}, {"mmm": 4}],
        "python_version": ["3.10", "3.11", "3.12"],
        "environment": "prod",
        "node": "node1",
    }
