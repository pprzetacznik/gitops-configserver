from os.path import join
import jinja2
import yaml
from gitops_mt.config import Config
from gitops_mt.utils import create_dir, read_file


class TenantsConfigLoader:
    def __init__(self, config):
        self.config = config

    def index(self):
        filepath = "index.yml"
        return self._load_yaml_file(filepath)

    def tenant(self, tenant_name):
        filepath = join(tenant_name, "index.yml")
        return self._load_yaml_file(filepath)

    def variables(self, tenant_name):
        filepath = join(tenant_name, "variables", "defaults.yml")
        return self._load_yaml_file(filepath)

    def _load_yaml_file(self, filename):
        filepath = join(self.config.CONFIG_DIR, filename)
        with open(filepath, "r") as f:
            content_dict = yaml.safe_load(f.read())
        return content_dict


class TemplatesRendering:

    def __init__(self, config: Config):
        self.config = config
        self.tenants_config_loader = TenantsConfigLoader(config)

        self.jinja_env = jinja2.Environment(
            block_start_string="\BLOCK{",
            block_end_string="}",
            variable_start_string="{",
            variable_end_string="}",
            comment_start_string="\#{",
            comment_end_string="}",
            line_statement_prefix="%%",
            line_comment_prefix="%#",
            trim_blocks=True,
            autoescape=False,
        )

    def render(self):
        create_dir(self.config.TARGET_DIR)
        tenants_list = self.tenants_config_loader.index().get("tenants", [])
        print(tenants_list)
        for tenant_name in tenants_list:
            variables = self.tenants_config_loader.variables(tenant_name)
            print(variables)
            tenant_config = self.tenants_config_loader.tenant(tenant_name)
            print(tenant_config)
            for template_config in tenant_config.get("configs"):
                print(template_config)
                template_content = read_file(
                    join(
                        self.config.CONFIG_DIR,
                        tenant_name,
                        "templates",
                        template_config.get("template_file"),
                    )
                )
                print(template_content)
                print(
                    self.render_template(
                        template_content,
                        {**variables, **{"template_var3": "123"}},
                    )
                )

    def render_template(self, template: str, variables: dict) -> dict:
        new_template = self.jinja_env.from_string(template)
        return new_template.render(**variables)
