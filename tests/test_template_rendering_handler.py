from pytest import fixture
from gitops_configserver.cli import TemplateRenderingHandler


@fixture
def args():
    class Args:
        config_dir = "resources/test_config"
        tenant_name = "tenant2"
        template_name = "build_variants.yaml"
        facts = '{"environment": "test"}'

    return Args()


@fixture
def template_rendering_handler():
    return TemplateRenderingHandler()


def test_template_rendering_handler(template_rendering_handler, args):
    assert (
        template_rendering_handler.execute(args)
        == """build:
  my_application:
    - env: test
      os: ubuntu22.04
      python: 3.12
    - env: test
      os: ubuntu22.04
      python: 3.13
    - env: test
      os: ubuntu24.04
      python: 3.12
    - env: test
      os: ubuntu24.04
      python: 3.13
    - env: dev
      os: ubuntu18.04
      python: python3.8"""
    )
