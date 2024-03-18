from flask import current_app, redirect, session, request
import os
import requests
from urllib.parse import urlencode

class SteamAuth:
    def init_app(self, app):
        @app.route("/auth")
        def auth_with_steam():
            params = {
                "openid.ns": "http://specs.openid.net/auth/2.0",
                "openid.identity": "http://specs.openid.net/auth/2.0/identifier_select",
                "openid.claimed_id": "http://specs.openid.net/auth/2.0/identifier_select",
                "openid.mode": "checkid_setup",
                "openid.return_to": request.url_root + "authorize",
                "openid.realm": request.url_root,
            }

            query_string = urlencode(params)
            auth_url = "https://steamcommunity.com/openid/login?" + query_string
            return redirect(auth_url)

        @app.route("/authorize")
        def authorize():
            STEAM_API_KEY = os.getenv("STEAM_API_KEY")
            if not STEAM_API_KEY:
                return "Steam API key not configured", 500

            steam_id = (request.args["openid.claimed_id"]).split("/")[-1]
            url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={STEAM_API_KEY}&steamids={steam_id}"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                player_info = data["response"]["players"][0]

                user_info = {
                    "steamid64": steam_id,
                    "steam_name": player_info["personaname"],
                    "avatar": player_info["avatarmedium"],
                    "country": player_info["loccountrycode"],
                }

                session["user_info"] = user_info
                
                return redirect("/")
            else:
                return "Failed to retrieve player information", 500

        @app.route("/signout")
        def signout():
            session.clear()
            return redirect("/")
