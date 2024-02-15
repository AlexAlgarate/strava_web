from __future__ import annotations

import os
import re
import webbrowser
from typing import Dict

import requests

from strava_web.utils import config as config
from strava_web.utils import err_log


class GetOauthCode:
    CLIENT_ID = os.getenv("CLIENT_ID")
    SECRET_CLIENT = os.getenv("SECRET_CLIENT")

    def get_code(self):
        header: Dict[str, str] = {
            "client_id": config.CLIENT_ID,
            "response_type": "code",
            "redirect_uri": config.redirect_url,
            "approval_prompt": "force",
            "scope": config.scopes,
        }

        code_request = requests.get(url=config.OAuth_url, data=header)
        webbrowser.open(code_request.url)
        """
        In web app, we paste the code in the input component.
        """
        # print("Paste here the URL from the browser: ", end="")
        raw_url: str = input().strip()

        code_match = re.search(r"&code=([\w]+)&", raw_url)

        if code_match:
            return code_match.group(1)
        else:
            err_log.error("Could not retrieve OAuth code from URL")
            return None
