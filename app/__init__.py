from flask import Flask, Blueprint
from app.api.v1.routes.parties.parties_route import parties_bp
from app.api.v1.routes.offices.offices_route import offices_bp

from Forum.configurations.config import app_config
#register blueprints

app = Flask(__name__)
def create_app(config_name):
    app.config.from_object(app_config[config_name])
    app.register_blueprint(parties_bp, url_prefix='/api/v1/')
    app.register_blueprint(offices_bp, url_prefix='/api/v1/')



    return app
