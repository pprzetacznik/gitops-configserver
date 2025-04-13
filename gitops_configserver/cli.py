from argparse import Namespace, ArgumentParser
from abc import ABC, abstractmethod
from logging import getLogger
from json import loads
from gitops_configserver.config import setup_logger, Config
from gitops_configserver.server import ConfigServer
from gitops_configserver.workflow import Workflow
from gitops_configserver.templates_rendering import TemplateRendering

logger = getLogger(__name__)


class AbstractArgumentsHandler(ABC):
    """Command pattern interface"""

    @abstractmethod
    def execute(self, args):
        raise NotImplementedError

    @abstractmethod
    def add_parser(self, subparsers):
        raise NotImplementedError


class TemplateRenderingHandler(AbstractArgumentsHandler):
    def execute(self, args):
        config = Config()
        config.CONFIG_DIR = args.config_dir
        result = TemplateRendering(config).render(
            args.tenant_name, args.template_name, loads(args.facts)
        )
        print(result)
        return result

    def add_parser(self, subparsers):
        parser_config_generator = subparsers.add_parser("template_gen")
        parser_config_generator.set_defaults(func=self.execute)
        parser_config_generator.add_argument(
            "--config_dir",
            type=str,
            help="Config directory",
            dest="config_dir",
            required=True,
        )
        parser_config_generator.add_argument(
            "--tenant_name",
            type=str,
            help="Tenant name",
            dest="tenant_name",
            required=True,
        )
        parser_config_generator.add_argument(
            "--template_name",
            type=str,
            help="Template name",
            dest="template_name",
            required=True,
        )
        parser_config_generator.add_argument(
            "--facts",
            type=str,
            help="Facts",
            dest="facts",
            default="{}",
            required=False,
        )


class ConfigGeneratorHandler(AbstractArgumentsHandler):
    def execute(self, args):
        config = Config()
        config.CONFIG_DIR = args.config_dir
        Workflow(config).execute()
        print('{"status": "ok"}')

    def add_parser(self, subparsers):
        parser_config_generator = subparsers.add_parser("config_gen")
        parser_config_generator.set_defaults(func=self.execute)
        parser_config_generator.add_argument(
            "--config_dir",
            type=str,
            help="Config directory",
            dest="config_dir",
            required=True,
        )
        parser_config_generator.add_argument(
            "--environment",
            type=str,
            help="Environment",
            dest="environment",
            default="dev",
            required=False,
        )


class ConfigServerHandler(AbstractArgumentsHandler):
    def execute(self, args):
        config = Config()
        config.CONFIG_DIR = args.config_dir
        config_server = ConfigServer(config)
        config_server.start()

    def add_parser(self, subparsers):
        parser_config_generator = subparsers.add_parser("server")
        parser_config_generator.set_defaults(func=self.execute)
        parser_config_generator.add_argument(
            "--config_dir",
            type=str,
            help="Config directory",
            dest="config_dir",
            required=True,
        )


def parse_arguments() -> Namespace:
    parser = ArgumentParser(
        description="GitOps multitenancy templates generator"
    )
    subparsers = parser.add_subparsers(required=True)
    handlers: list[type] = [
        TemplateRenderingHandler,
        ConfigGeneratorHandler,
        ConfigServerHandler,
    ]
    for handler in handlers:
        handler().add_parser(subparsers)
    return parser.parse_args()


def main() -> None:
    setup_logger()
    args = parse_arguments()
    args.func(args)


if __name__ == "__main__":
    main()
