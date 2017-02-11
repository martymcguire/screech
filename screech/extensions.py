from flask_micropub import MicropubClient

micropub = MicropubClient()

def init_app(app):
    micropub.init_app(app, app.config["CLIENT_NAME"])
