from typing import Dict, Union

import requests

from strava_web.src.strava_api.get_token.request_credentials import RequestAccessToken
from strava_web.utils import exc_log


class RequestActivities:
    url: str

    def __init__(self, api_url: str) -> None:
        self.api_url: str = api_url
        self.access_token = RequestAccessToken().generate_token()

    def get_activity(
        self,
        page: int = 1,
        page_size: int = 200,
    ) -> Dict[str, Union[int, str]]:
        try:
            params: Dict[str, Union[int, str]] = {
                "access_token": self.access_token,
                "per_page": page_size,
                "page": page,
            }
            response: requests.Response = requests.get(
                self.api_url,
                params=params,
            )
            response.raise_for_status()
            return response.json()

        except Exception as e:
            exc_log.exception(f"Error: {e}")
            raise
