from jinja2 import Environment, StrictUndefined
from jinja2.exceptions import UndefinedError
from gitops_configserver.config import Config
from gitops_configserver.templates_rendering import TenantsConfigLoader


class HieradataResolver:

    def __init__(self, config: Config):
        self.config = config
        self.tenants_config_loader = TenantsConfigLoader(config)
        self.jinja_env = Environment(
            variable_start_string="{",
            variable_end_string="}",
            undefined=StrictUndefined,
        )

    def _resolve_hierarchy(self, hierarchy: list, facts: dict) -> list:
        resolved_hierarchy = []
        for hiera in hierarchy:
            try:
                resolved_hierarchy += [
                    self.jinja_env.from_string(hiera).render(**facts)
                ]
            except UndefinedError:
                pass
        return resolved_hierarchy

    def render(self, tenant_name: str, facts: dict) -> dict:
        index = self.tenants_config_loader.index()
        hierarchy = index.get("hierarchy")
        resolved_hierarchy = self._resolve_hierarchy(hierarchy, facts)
        final_variables: dict = {}
        for hiera in reversed(resolved_hierarchy):
            overlay_variables = self.tenants_config_loader.variables(
                tenant_name, hiera
            )
            final_variables = {**final_variables, **overlay_variables}
        return final_variables
