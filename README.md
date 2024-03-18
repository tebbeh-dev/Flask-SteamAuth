# !!This extension is NOT yet published!!
If you are going to use this before I published it to pypi.org you will need to do it manually. I will remove this when its uploaded.

# What is Flask-SteamAuth
Flask-SteamAuth is a fully integrated method for authenticate with your Steam account, return user information and create a logged in session in your Flask app.

# Getting started
1. Create a new project and navigate to it
```
# Windows
cd C:\path\to\project-folder

# Linux
mkdir /path/to/project-folder && cd /path/to/project-folder
```

2. Create a virtual environment

Linux
```
python3 -m venv venv
```
```
source venv/bin/activate
```
Windows
```
python -m venv venv
```
```
.\venv\Scripts\activate
```

3. Install Flask-SteamAuth
```
pip install Flask-SteamAuth
```
4. Create a Flask App
With dotenv (recommend)
```py
from flask import Flask, session
from flask_steamauth import SteamAuth
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
steam_auth = SteamAuth()

steam_auth.init_app(app)

STEAM_API_KEY = os.getenv("STEAM_API_KEY")

@app.route('/')
def index():

    # Logged in user information will be stored in "session", see below example
    user_info = session.get("user_info")
    
    if user_info is None:
        return "Hello World!<br><a href='/auth'>Sign in to steam</a>"
    else:
        return f"Welcome <b>{user_info['steam_name']}</b>!<br>avatar: <img src='{user_info['avatar']}'><br>steamid64: {user_info['steamid64']}<br>country: {user_info['country']}<br><a href='/auth'>Sign out from steam</a>"

if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'your_secret_key'  
    app.config["STEAM_API_KEY"] = STEAM_API_KEY
    app.run(debug=True)
```

Without dotenv (not hidden token)
```py
from flask import Flask, session
from flask_steamauth import SteamAuth

load_dotenv()

app = Flask(__name__)
steam_auth = SteamAuth()

steam_auth.init_app(app)

@app.route('/')
def index():

    # Logged in user information will be stored in "session", see below example
    user_info = session.get("user_info")
    
    if user_info is None:
        return "Hello World!<br><a href='/auth'>Sign in to steam</a>"
    else:
        return f"Welcome <b>{user_info['steam_name']}</b>!<br>avatar: <img src='{user_info['avatar']}'><br>steamid64: {user_info['steamid64']}<br>country: {user_info['country']}<br><a href='/auth'>Sign out from steam</a>"

if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'your_secret_key'  
    app.config["STEAM_API_KEY"] = 'your_steam_id_key'
    app.run(debug=True)
```

5. Save your file and run it with Python
