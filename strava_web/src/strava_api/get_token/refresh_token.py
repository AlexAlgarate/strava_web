from time import time
from typing import Dict, Tuple, Union

import requests
from requests.exceptions import ConnectionError, ConnectTimeout, HTTPError, Timeout

from strava_web.utils import exc_log
from strava_web.utils.config import EXPIRES_AT, refresh_data, token_url


class RefreshTokenManager:
    def __init__(self) -> None:
        self.current_time: int = int(time())

    def _check_expired(self) -> bool:
        try:
            expires_at: int = int(EXPIRES_AT)
            return expires_at < self.current_time

        except Exception as e:
            exc_log.exception(f"An unexpected error occurred: {e}")
            raise

    def _request_refresh_token(
        self,
        params: Dict[str, Union[str, int]],
    ) -> requests.Response:
        return requests.post(url=token_url, data=params)

    def _parse_refresh_request(
        self, refresh_response: requests.Response
    ) -> Dict[str, Union[str, int]]:
        refresh_response.raise_for_status()
        data = refresh_response.json()

        for key in ("access_token", "refresh_token", "expires_at"):
            if key not in data:
                raise ValueError("Missing key in response data: " + key)
        return data

    def _extract_credentials(
        self,
        data: Dict[str, Union[str, int]],
    ) -> Tuple[str, int]:
        access_token: str = data.get("access_token")

        return access_token

    def refresh_access_token(self) -> str:
        try:
            params: Dict[str, str | int] = refresh_data
            request: requests.Response = self._request_refresh_token(params)
            response: Dict[str, str | int] = self._parse_refresh_request(request)
            access_token = self._extract_credentials(response)
            return access_token

        except (HTTPError, ConnectTimeout, Timeout, ConnectionError) as e:
            exc_log.exception(f"Error: {e}. {type(e)} occurred.")
            raise
        except Exception as e:
            exc_log.exception(f"Error: {e}. {type(e)} occurred.")
            raise
