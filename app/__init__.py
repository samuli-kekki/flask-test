from flask import Flask
import os
from .routes import measurement_blueprint

def create_app():
    app = Flask(__name__)

    # DB_URL is specified in docker-compose.yml.
    # For production, it would have to be specified in Kubernetes Pod manifest, etc.
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URL")

    app.register_blueprint(measurement_blueprint)

    return app
