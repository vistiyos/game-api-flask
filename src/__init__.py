
from dotenv import load_dotenv
from flask import Flask

from src.infrastructure import (
    init_config,
    init_marshmallow,
    initialize_db,
    register_routes,
)


def create_app(test_config = None):
    """Factory to create the Flask application
    :return: A `Flask` application instance
    """
    load_dotenv()

    app = Flask(__name__)

    init_config(app)

    if test_config:
        app.config.update(test_config)

    register_routes(app)
    initialize_db(app)
    init_marshmallow(app)
    return app
