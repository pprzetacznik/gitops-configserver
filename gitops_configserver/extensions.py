from flask import Flask


class ConfigProvider:
    def init_app(self, app):
        self.app = app

    def get_app(self) -> Flask:
        return self.app


config_provider = ConfigProvider()
