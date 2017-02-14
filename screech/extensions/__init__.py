from flask_micropub import MicropubClient
from .micropub_config import MicropubConfig

micropub = MicropubClient()
micropub_config = MicropubConfig

def init_app(app):
    micropub.init_app(app, app.config["CLIENT_NAME"])
