import requests
from typing import Optional
from thornode_py.models.thronode_models_auth import THORNodeAccountsResponse
from thornode_py.models.thronode_models_bank import THORNodeBalancesResponse
from thornode_py.models.thronode_models_health import THORNodePing
from thornode_py.models.thronode_models_liquidiry_provider import THORNodeLiquidityProvider, THORNodeLiquidityProviderSummary
from thornode_py.models.thronode_models_node import THORNodeNode
from thornode_py.models.thronode_models_pool import THORNodePool, THORNodeDerivedPool
from thornode_py.models.thronode_models_pool_slip import THORNodePoolSlip
from thornode_py.models.thronode_models_rune_pool import THORNodeRunePool, THORNodeRuneProvider
from thornode_py.models.thronode_models_tcy_claimer import THORNodeTcyClaimerResult, THORNodeTcyClaimersResult
from thornode_py.models.thronode_models_tcy_staker import THORNodeTcyStaker, THORNodeTcyStakersResult
from thornode_py.models.thronode_models_thorname import THORNodeThorname
from thornode_py.models.thronode_models_saver import THORNodeSaver


class THORNodeAPI:
    def __init__(self, base_url: str = "https://thornode.ninerealms.com", timeout: int = 15):
        self.base_url = base_url
        self.timeout = timeout

    # Auth
    #-------------------------------------------------------------------------------------------------------------------
    def accounts(self, address: str, height: Optional[int] = None) -> THORNodeAccountsResponse:
        url = f"{self.base_url}/auth/accounts/{address}"
        params = {"height": height} if height is not None else None
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return THORNodeAccountsResponse.model_validate(data)
    #-------------------------------------------------------------------------------------------------------------------



    # Bank
    #-------------------------------------------------------------------------------------------------------------------
    def balances(self, address: str, height: Optional[int] = None) -> THORNodeBalancesResponse:
        url = f"{self.base_url}/bank/balances/{address}"
        params = {"height": height} if height is not None else None
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return THORNodeBalancesResponse.model_validate(data)
    #-------------------------------------------------------------------------------------------------------------------



    # Health
    #-------------------------------------------------------------------------------------------------------------------
    def ping(self) -> THORNodePing:
        url = f"{self.base_url}/thorchain/ping"
        response = requests.get(url, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return THORNodePing.model_validate(data)
    #-------------------------------------------------------------------------------------------------------------------

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



    # Pool Slip
    #-------------------------------------------------------------------------------------------------------------------
    def slip(self, asset: str, height: Optional[int] = None) -> list[THORNodePoolSlip]:
        url = f"{self.base_url}/thorchain/slip/{asset}"
        params = {"height": height} if height is not None else None
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return [THORNodePoolSlip.model_validate(item) for item in data]

    def slips(self, height: Optional[int] = None) -> list[THORNodePoolSlip]:
        url = f"{self.base_url}/thorchain/slips"
        params = {"height": height} if height is not None else None
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return [THORNodePoolSlip.model_validate(item) for item in data]
    #-------------------------------------------------------------------------------------------------------------------



    # Liquidity Providers
    #-------------------------------------------------------------------------------------------------------------------
    def liquidity_provider(self, asset: str, address: str, height: Optional[int] = None) -> THORNodeLiquidityProvider:
        url = f"{self.base_url}/thorchain/pool/{asset}/liquidity_provider/{address}"
        params = {"height": height} if height is not None else None
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return THORNodeLiquidityProvider.model_validate(data)

    def liquidity_providers(self, asset: str, height: Optional[int] = None) -> list[THORNodeLiquidityProviderSummary]:
        url = f"{self.base_url}/thorchain/pool/{asset}/liquidity_providers"
        params = {"height": height} if height is not None else None
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return [THORNodeLiquidityProviderSummary.model_validate(item) for item in data]
    #-------------------------------------------------------------------------------------------------------------------



    # TCY Stakers
    #-------------------------------------------------------------------------------------------------------------------
    def tcy_staker(self, address: str, height: Optional[int] = None) -> THORNodeTcyStaker:
        url = f"{self.base_url}/thorchain/tcy_staker/{address}"
        params = {"height": height} if height is not None else None
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return THORNodeTcyStaker.model_validate(data)

    def tcy_stakers(self, height: Optional[int] = None) -> THORNodeTcyStakersResult:
        url = f"{self.base_url}/thorchain/tcy_stakers"
        params = {"height": height} if height is not None else None
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return THORNodeTcyStakersResult.model_validate(data)
    #-------------------------------------------------------------------------------------------------------------------



    # TCY Claimers
    #-------------------------------------------------------------------------------------------------------------------
    def tcy_claimer(self, address: str, height: Optional[int] = None) -> THORNodeTcyClaimerResult:
        url = f"{self.base_url}/thorchain/tcy_claimer/{address}"
        params = {"height": height} if height is not None else None
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return THORNodeTcyClaimerResult.model_validate(data)

    def tcy_claimers(self, height: Optional[int] = None) -> THORNodeTcyClaimersResult:
        url = f"{self.base_url}/thorchain/tcy_claimers"
        params = {"height": height} if height is not None else None
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return THORNodeTcyClaimersResult.model_validate(data)
    #-------------------------------------------------------------------------------------------------------------------



    # RUNE Pool
    #-------------------------------------------------------------------------------------------------------------------
    def runepool(self, height: Optional[int] = None) -> THORNodeRunePool:
        url = f"{self.base_url}/thorchain/runepool"
        params = {"height": height} if height is not None else None
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return THORNodeRunePool.model_validate(data)

    def rune_provider(self, address: str, height: Optional[int] = None) -> THORNodeRuneProvider:
        url = f"{self.base_url}/thorchain/rune_provider/{address}"
        params = {"height": height} if height is not None else None
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return THORNodeRuneProvider.model_validate(data)

    def rune_providers(self, height: Optional[int] = None) -> list[THORNodeRuneProvider]:
        url = f"{self.base_url}/thorchain/rune_providers"
        params = {"height": height} if height is not None else None
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return [THORNodeRuneProvider.model_validate(item) for item in data]
    #-------------------------------------------------------------------------------------------------------------------



    # Savers
    #-------------------------------------------------------------------------------------------------------------------
    def saver(self, asset: str, address: str, height: Optional[int] = None) -> THORNodeSaver:
        url = f"{self.base_url}/thorchain/pool/{asset}/saver/{address}"
        params = {"height": height} if height is not None else None
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return THORNodeSaver.model_validate(data)

    def savers(self, asset: str, height: Optional[int] = None) -> list[THORNodeSaver]:
        url = f"{self.base_url}/thorchain/pool/{asset}/savers"
        params = {"height": height} if height is not None else None
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return [THORNodeSaver.model_validate(item) for item in data]
    #-------------------------------------------------------------------------------------------------------------------



    # Borrowers
    #-------------------------------------------------------------------------------------------------------------------

    #-------------------------------------------------------------------------------------------------------------------



    # Transactions
    #-------------------------------------------------------------------------------------------------------------------

    #-------------------------------------------------------------------------------------------------------------------



    # Nodes
    #-------------------------------------------------------------------------------------------------------------------
    def node(self, address: str, height: Optional[int] = None) -> THORNodeNode:
        url = f"{self.base_url}/thorchain/node/{address}"
        params = {"height": height} if height is not None else None
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return THORNodeNode.model_validate(data)

    def nodes(self, height: Optional[int] = None) -> list[THORNodeNode]:
        url = f"{self.base_url}/thorchain/nodes"
        params = {"height": height} if height is not None else None
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return [THORNodeNode.model_validate(item) for item in data]
    #-------------------------------------------------------------------------------------------------------------------



    # Vaults
    #-------------------------------------------------------------------------------------------------------------------

    #-------------------------------------------------------------------------------------------------------------------
