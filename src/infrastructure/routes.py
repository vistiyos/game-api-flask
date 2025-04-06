from flask import Flask
from flask_smorest import Api
from src.api.controllers import game_api

def register_routes(app: Flask) -> None:
    api = Api(app)
    api.register_blueprint(game_api)