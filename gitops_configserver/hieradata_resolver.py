from logging import getLogger
from jinja2 import Environment, StrictUndefined
from jinja2.exceptions import UndefinedError
from gitops_configserver.config import Config
from gitops_configserver.config_loader import TenantsConfigLoader


logger = getLogger(__name__)


class HieradataResolver:

    def __init__(self, config: Config):
        self.config = config
        self.tenants_config_loader = TenantsConfigLoader(config)
        self.jinja_env = Environment(
            variable_start_string="{",
            variable_end_string="}",
            undefined=StrictUndefined,
        )

    def _merge(self, source: dict, destination: dict) -> dict:
        for source_key, source_value in source.items():
            if isinstance(source_value, dict):
                destination[source_key] = self._merge(
                    source_value, destination.get(source_key, {})
                )
            else:
                destination[source_key] = source_value
        return destination

    def _resolve_hierarchy(self, hierarchy: list, facts: dict) -> list:
        resolved_hierarchy = []
        for hiera in hierarchy:
            try:
                resolved_hierarchy += [
                    self.jinja_env.from_string(hiera).render(**facts)
                ]
            except UndefinedError:
                logger.info(
                    "Some facts were not defined during resolution of hieradata structure"
                )
        return resolved_hierarchy

    def render(self, tenant_name: str, facts: dict) -> dict:
        index = self.tenants_config_loader.index()
        hierarchy = index.get("hierarchy", [])
        resolved_hierarchy = self._resolve_hierarchy(hierarchy, facts)
        final_variables: dict = {}
        for hiera in reversed(resolved_hierarchy):
            overlay_variables = self.tenants_config_loader.variables(
                tenant_name, hiera
            )
            final_variables = self._merge(overlay_variables, final_variables)
        return final_variables
