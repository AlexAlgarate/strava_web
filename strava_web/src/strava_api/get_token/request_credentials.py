import os

import requests
from dotenv import load_dotenv

# from strava_web.src.strava_api.tokens_process.oauth_code.get_oauth_code import (
#     GetOauthCode,
# )
from strava_web.src.strava_api.get_token.get_oauth_code import GetOauthCode
from strava_web.utils import config as config


class RequestAccessToken:
    load_dotenv()

    CLIENT_ID = os.environ.get("CLIENT_ID")
    SECRET_CLIENT = os.environ.get("SECRET_CLIENT")
    URL = config.token_url

    def __init__(self) -> None:
        self.code = GetOauthCode()
        self.token = None

    def generate_token(self) -> str:
        response = requests.post(
            url=self.URL,
            data={
                "client_id": self.CLIENT_ID,
                "client_secret": self.SECRET_CLIENT,
                "code": self.code.get_code(),
                "grant_type": "authorization_code",
            },
            # data={
            #     "client_id": self.CLIENT_ID,
            #     "client_secret": self.SECRET_CLIENT,
            #     "code": self.code.get_oauth_code(),
            #     "grant_type": "authorization_code",
            # },
        )
        if response.status_code == 200:
            self.token = response.json()["access_token"]
            return self.token
        else:
            self.token = None
