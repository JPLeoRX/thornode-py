import requests
from typing import Optional
from thornode_py.thronode_models import (
    THORNodePing,
    THORNodeThorname,
    THORNodeBalancesResponse,
    THORNodeAccountsResponse,
    THORNodePool,
    THORNodeDerivedPool,
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

    # Pools
    #-------------------------------------------------------------------------------------------------------------------
    def pool(self, asset: str, height: Optional[int] = None) -> THORNodePool:
        url = f"{self.base_url}/thorchain/pool/{asset}"
        params = {"height": height} if height is not None else None
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return THORNodePool.model_validate(data)

    def pools(self, height: Optional[int] = None) -> list[THORNodePool]:
        url = f"{self.base_url}/thorchain/pools"
        params = {"height": height} if height is not None else None
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return [THORNodePool.model_validate(item) for item in data]

    def dpool(self, asset: str, height: Optional[int] = None) -> THORNodeDerivedPool:
        url = f"{self.base_url}/thorchain/dpool/{asset}"
        params = {"height": height} if height is not None else None
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return THORNodeDerivedPool.model_validate(data)

    def dpools(self, height: Optional[int] = None) -> list[THORNodeDerivedPool]:
        url = f"{self.base_url}/thorchain/dpools"
        params = {"height": height} if height is not None else None
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return [THORNodeDerivedPool.model_validate(item) for item in data]
    #-------------------------------------------------------------------------------------------------------------------
