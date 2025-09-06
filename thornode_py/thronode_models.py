from pydantic import BaseModel
from typing import List, Optional


class THORNodePing(BaseModel):
    ping: str


# Thorname
#-----------------------------------------------------------------------------------------------------------------------
class THORNodeThornameAlias(BaseModel):
    chain: str
    address: str


class THORNodeThorname(BaseModel):
    name: str
    expire_block_height: int
    owner: str
    preferred_asset: str
    preferred_asset_swap_threshold_rune: str
    affiliate_collector_rune: str
    aliases: List[THORNodeThornameAlias]
#-----------------------------------------------------------------------------------------------------------------------



# Bank
#-----------------------------------------------------------------------------------------------------------------------
class THORNodeBalanceAmount(BaseModel):
    denom: str
    amount: str


class THORNodeBalancesResponse(BaseModel):
    result: List[THORNodeBalanceAmount]
#-----------------------------------------------------------------------------------------------------------------------



# Auth
#-----------------------------------------------------------------------------------------------------------------------
class THORNodeAccount(BaseModel):
    address: str
    pub_key: str
    account_number: str
    sequence: str


class THORNodeAccountResult(BaseModel):
    value: THORNodeAccount


class THORNodeAccountsResponse(BaseModel):
    result: THORNodeAccountResult
#-----------------------------------------------------------------------------------------------------------------------



# Pools
#-----------------------------------------------------------------------------------------------------------------------
class THORNodePool(BaseModel):
    asset: str
    short_code: Optional[str] = None
    status: str
    decimals: Optional[int] = 6
    pending_inbound_asset: str
    pending_inbound_rune: str
    balance_asset: str
    balance_rune: str
    asset_tor_price: str
    pool_units: str
    LP_units: str
    synth_units: str
    synth_supply: str
    savers_depth: str
    savers_units: str
    savers_fill_bps: str
    savers_capacity_remaining: str
    synth_mint_paused: bool
    synth_supply_remaining: str
    loan_collateral: str
    loan_collateral_remaining: str
    loan_cr: str
    derived_depth_bps: str
    trading_halted: bool

class THORNodeDerivedPool(BaseModel):
    asset: str
    status: str
    balance_asset: str
    balance_rune: str
    derived_depth_bps: str
#-----------------------------------------------------------------------------------------------------------------------
