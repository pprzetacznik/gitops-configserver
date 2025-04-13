from os.path import join
from logging import getLogger
from yaml import safe_load
from gitops_configserver.config import Config

logger = getLogger(__name__)


class TenantsConfigLoader:
    def __init__(self, config: Config):
        self.config = config

    def index(self) -> dict:
        filepath = "index.yaml"
        return self._load_yaml_file(filepath) or {}

    def tenant(self, tenant_name) -> dict:
        filepath = join(tenant_name, "index.yaml")
        return self._load_yaml_file(filepath) or {}

    def variables(self, tenant_name, variable_file="defaults.yaml") -> dict:
        filepath = join(tenant_name, "variables", variable_file)
        return self._load_yaml_file(filepath) or {}

    def _load_yaml_file(self, filename):
        filepath = join(self.config.CONFIG_DIR, filename)
        try:
            with open(filepath, "r") as f:
                content_dict = safe_load(f.read())
        except FileNotFoundError:
            logger.info(f"File: {filepath} not found")
            content_dict = {}
        return content_dict
