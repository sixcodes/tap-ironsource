# from datetime import datetime
from dateutil import parser
from typing import Dict
import requests


class IronsourceClient:

    def __init__(self, config: Dict[str, str]) -> None:
        self.base_url = 'https://platform.ironsrc.com/'
        self.config = config
        self.auth_token: str = self.__request_auth_token()


    def __request_auth_token(self) -> str:
        return (requests
            .get(f"{self.base_url}/partners/publisher/auth", headers={
                "secretKey": self.config.get("secret_key"),
                "refreshToken": self.config.get("refresh_token"),
            })
            .json())


    def get_reports(self, start_date: str, end_date: str) -> Dict[str, str]:
        url = f"{self.base_url}/partners/publisher/mediation/applications/v6/stats"
        headers = {
            "Authorization": f"Bearer {self.auth_token}",
        }
        params = {
            "startDate": parser.parse(start_date).strftime("%Y-%m-%d"),
            "endDate": parser.parse(end_date).strftime("%Y-%m-%d"),
            "appKey": self.config.get("app_key"),
        }

        res = (requests
            .get(url=url, headers=headers, params=params))

        print(res.status_code)

        return res.content
