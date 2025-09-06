import requests
from typing import Optional
from thornode_py.thronode_models import (
    THORNodePing,
    THORNodeThorname,
    THORNodeBalancesResponse,
    THORNodeAccountsResponse,
)


class THORNodeAPI:
    def __init__(self, base_url: str = "https://thornode.ninerealms.com", timeout: int = 15):
        self.base_url = base_url
        self.timeout = timeout

    # Auth
    def accounts(self, address: str, height: Optional[int] = None) -> THORNodeAccountsResponse:
        url = f"{self.base_url}/auth/accounts/{address}"
        params = {"height": height} if height is not None else None
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return THORNodeAccountsResponse.model_validate(data)

    # Bank
    def balances(self, address: str, height: Optional[int] = None) -> THORNodeBalancesResponse:
        url = f"{self.base_url}/bank/balances/{address}"
        params = {"height": height} if height is not None else None
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return THORNodeBalancesResponse.model_validate(data)

    # Health
    def ping(self) -> THORNodePing:
        url = f"{self.base_url}/thorchain/ping"
        response = requests.get(url, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return THORNodePing.model_validate(data)

    # Thornames
    def thorname(self, name: str, height: Optional[int] = None) -> THORNodeThorname:
        url = f"{self.base_url}/thorchain/thorname/{name}"
        params = {"height": height} if height is not None else None
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return THORNodeThorname.model_validate(data)

