from os.path import join
from yaml import safe_load
from flask import Blueprint, jsonify, request
from flask_restful import Resource
from typing import Optional
from gitops_configserver.extensions import config_provider
from gitops_configserver.utils import load_yaml
from gitops_configserver.config import Config
from gitops_configserver.templates_rendering import TemplateRendering

blueprint = Blueprint("configs", __name__)


class ConfigsAPI(Resource):
    def get(self):
        config = config_provider.get_app().config["config"]
        filename = join(config.CONFIG_DIR, "index.yaml")
        index = load_yaml(filename)
        return jsonify(index)


class TenantConfigsAPI(Resource):
    def get(self, tenant_name: str, template_name: str):
        config = config_provider.get_app().config["config"]
        facts = {}
        if request.is_json:
            facts = request.json
        result = TemplateRendering(config).render(
            tenant_name, template_name, facts
        )
        index = safe_load(result)
        return jsonify(index)


blueprint.add_url_rule(
    "/configs",
    view_func=ConfigsAPI.as_view("configs"),
    methods=["GET"],
)
blueprint.add_url_rule(
    "/configs/<string:tenant_name>/<string:template_name>",
    view_func=TenantConfigsAPI.as_view("tenant_configs"),
    methods=["GET"],
)
