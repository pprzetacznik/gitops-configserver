from abc import ABC, abstractmethod
from gitops_configserver.templates_rendering import (
    TemplatesRendering,
    TenantsConfigLoader,
    MatrixResolver,
)
from gitops_configserver.utils import create_dir


class WorkflowCommand(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class TemplatesRenderingCommand:
    def __init__(self, config):
        self.config = config
        self.tenants_config_loader = TenantsConfigLoader(config)

    def execute(self) -> None:
        create_dir(self.config.TARGET_DIR)
        tenants_list = self.tenants_config_loader.index().get("tenants", [])
        print(tenants_list)
        for tenant_name in tenants_list:
            templates_rendering = TemplatesRendering(self.config)
            templates_rendering.render(tenant_name)


class Workflow:
    def __init__(self, config):
        self.config = config

    def execute(self) -> None:
        commands = [
            TemplatesRenderingCommand,
        ]
        for command in commands:
            command(self.config).execute()
