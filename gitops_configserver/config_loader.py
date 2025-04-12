from os.path import join
from yaml import safe_load
from gitops_configserver.config import Config


class TenantsConfigLoader:
    def __init__(self, config: Config):
        self.config = config

    def index(self):
        filepath = "index.yml"
        return self._load_yaml_file(filepath)

    def tenant(self, tenant_name):
        filepath = join(tenant_name, "index.yml")
        return self._load_yaml_file(filepath)

    def variables(self, tenant_name, variable_file="defaults.yml"):
        filepath = join(tenant_name, "variables", variable_file)
        return self._load_yaml_file(filepath)

    def _load_yaml_file(self, filename):
        filepath = join(self.config.CONFIG_DIR, filename)
        with open(filepath, "r") as f:
            content_dict = safe_load(f.read())
        return content_dict
