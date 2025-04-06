from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def initialize_db(app):
    """Initialize the database and migrations."""
    db.init_app(app)
    Migrate(app, db)