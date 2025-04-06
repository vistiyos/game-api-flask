
import pytest
from flask_migrate import upgrade
from testcontainers.postgres import PostgresContainer

from src import create_app
from src.infrastructure.db import db


@pytest.fixture(scope="module")
def app():
    with PostgresContainer("postgres:16") as postgres:
        app = create_app({
            "SQLALCHEMY_DATABASE_URI": postgres.get_connection_url()
        })

        with app.app_context():
            upgrade()

        yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def db_interface(app):
    with app.app_context():
        yield db