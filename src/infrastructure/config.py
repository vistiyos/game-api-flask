import os

from flask import Flask

class Config:
    def __init__(self):
        self.ENV = os.environ.get("ENV")
        self.DEBUG = os.environ.get("DEBUG")
        self.PORT = os.environ.get("PORT")
        self.HOST = "0.0.0.0"
        self.SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")
        self.API_TITLE = "Game-API"
        self.API_VERSION = "0.0.1"
        self.OPENAPI_VERSION = "3.0.2"
        self.OPENAPI_URL_PREFIX = "/docs"
        self.LOGGING_LEVEL = os.environ.get("LOGGING_LEVEL", "INFO")

def init_config(app: Flask):
    configuration = Config()
    app.logger.setLevel(configuration.LOGGING_LEVEL)

    app.config.from_object(configuration)
    app.env = configuration.ENV