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



# Pool Slips
#-----------------------------------------------------------------------------------------------------------------------
class THORNodePoolSlip(BaseModel):
    asset: str
    pool_slip: int
    rollup_count: int
    long_rollup: int
    rollup: int
    summed_rollup: Optional[int] = None
#-----------------------------------------------------------------------------------------------------------------------



# TCY Stakers
#-----------------------------------------------------------------------------------------------------------------------
class THORNodeTCYStaker(BaseModel):
    address: str
    amount: str

class THORNodeTCYStakersResult(BaseModel):
    tcy_stakers: List[THORNodeTCYStaker]
#-----------------------------------------------------------------------------------------------------------------------



# TCY Claimers
#-----------------------------------------------------------------------------------------------------------------------
class THORNodeTCYClaimer(BaseModel):
    l1_address: Optional[str] = None
    amount: str
    asset: str


class THORNodeTCYClaimersResult(BaseModel):
    tcy_claimers: List[THORNodeTCYClaimer]

class THORNodeTCYClaimerResult(BaseModel):
    tcy_claimer: List[THORNodeTCYClaimer]
#-----------------------------------------------------------------------------------------------------------------------



# Nodes
#-----------------------------------------------------------------------------------------------------------------------
class THORNodePubKeySet(BaseModel):
    secp256k1: Optional[str] = None
    ed25519: Optional[str] = None


class THORNodeBondProvider(BaseModel):
    bond_address: str
    bond: str


class THORNodeBondProviders(BaseModel):
    node_operator_fee: str
    providers: Optional[List[THORNodeBondProvider]] = []


class THORNodeChainHeight(BaseModel):
    chain: str
    height: int


class THORNodeJail(BaseModel):
    release_height: Optional[int] = None
    reason: Optional[str] = None


class THORNodePreflightStatus(BaseModel):
    status: str
    reason: str
    code: int


class THORNodeNode(BaseModel):
    node_address: str
    status: str
    pub_key_set: THORNodePubKeySet
    validator_cons_pub_key: str
    peer_id: str
    active_block_height: int
    status_since: int
    node_operator_address: str
    total_bond: str
    bond_providers: THORNodeBondProviders
    signer_membership: Optional[List[str]] = []
    requested_to_leave: bool
    forced_to_leave: bool
    leave_height: int
    ip_address: str
    version: str
    slash_points: int
    jail: THORNodeJail
    current_award: str
    observe_chains: Optional[List[THORNodeChainHeight]] = []
    maintenance: bool
    missing_blocks: int
    preflight_status: THORNodePreflightStatus
#-----------------------------------------------------------------------------------------------------------------------



# Liquidity Providers
#-----------------------------------------------------------------------------------------------------------------------
class THORNodeLiquidityProviderSummary(BaseModel):
    asset: str
    units: str
    pending_rune: str
    pending_asset: str
    rune_deposit_value: str
    asset_deposit_value: str
    rune_address: Optional[str] = None
    asset_address: Optional[str] = None
    last_add_height: Optional[int] = None
    last_withdraw_height: Optional[int] = None
    pending_tx_id: Optional[str] = None


class THORNodeLiquidityProvider(BaseModel):
    asset: str
    units: str
    pending_rune: str
    pending_asset: str
    rune_deposit_value: str
    asset_deposit_value: str
    rune_address: Optional[str] = None
    asset_address: Optional[str] = None
    last_add_height: Optional[int] = None
    last_withdraw_height: Optional[int] = None
    pending_tx_id: Optional[str] = None
    rune_redeem_value: Optional[str] = None
    asset_redeem_value: Optional[str] = None
    luvi_deposit_value: Optional[str] = None
    luvi_redeem_value: Optional[str] = None
    luvi_growth_pct: Optional[str] = None
#-----------------------------------------------------------------------------------------------------------------------
