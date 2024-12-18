from flask import Flask
import os
from .routes import measurement_blueprint
from flask_sqlalchemy import SQLAlchemy

# We store db reference here, maybe could store somewhere else?
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # DB_URL is specified in docker-compose.yml.
    # For production, it would have to be specified in Kubernetes Pod manifest, etc.
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URL")

    # Register db with the app
    db.init_app(app)

    # Register blueprint (request routes) with the app
    app.register_blueprint(measurement_blueprint)

    # Need to "push" the context since this is outside of request
    with app.app_context():
        # For this test, we are just dropping the schema
        # and creating it all over again.
        db.drop_all()
        db.create_all()

    return app
