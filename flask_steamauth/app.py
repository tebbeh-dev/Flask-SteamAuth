import os
from flask import Flask
from .steamauth import SteamAuth

def create_app():
    app = Flask(__name__)
    SteamAuth().init_app(app)

    # Ensure STEAM_API_KEY is set in environment variables
    if 'STEAM_API_KEY' not in os.environ:
        raise EnvironmentError("[SteamAuth] STEAM_API_KEY environment variable is not set")

    # Set STEAM_API_KEY from environment variable
    app.config['STEAM_API_KEY'] = os.environ['STEAM_API_KEY']

    return app

if __name__ == '__main__':
    create_app().run()