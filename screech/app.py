from . import extensions
from .views import views
from .api import api
from flask import Flask
import logging
import sys

def create_app(config_path='../screech.cfg'):
    app = Flask('screech')
    app.config.from_pyfile(config_path)
    configure_logging(app)
    extensions.init_app(app)
    app.register_blueprint(views)
    app.register_blueprint(api, url_prefix='/api')
    return app

def configure_logging(app):
    if app.debug:
        return

    app.logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
