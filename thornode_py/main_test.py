from thornode_api import THORNodeAPI

api = THORNodeAPI()


# print("Liquidity Providers:")
# print(len(api.liquidity_providers("BTC.BTC")))
# print(api.liquidity_provider("BTC.BTC", "bc1q00nrswtpp3zddgc0uvppuszhnr8k8zfcdps9gn"))

# TCY Stakers
tcy_stakers = api.tcy_stakers()
print(f"TCY Staker: api.tcy_stakers() call found {len(tcy_stakers.tcy_stakers)} results")
tcy_staker = api.tcy_staker(tcy_stakers.tcy_stakers[0].address)
print(f"TCY Staker: api.tcy_staker() call found {tcy_staker} result")

# TCY Claimers
tcy_claimers = api.tcy_claimers()
print(f"TCY Claimer: api.tcy_claimers() call found {len(tcy_claimers.tcy_claimers)} results")
tcy_claimer = api.tcy_claimer(tcy_claimers.tcy_claimers[0].l1_address)
print(f"TCY Claimer: api.tcy_claimer() call found {tcy_claimer} result")


# RUNE Pool
runepool = api.runepool()
print(f"RUNE Pool: api.runepool() returned {runepool}")

# RUNE Providers
providers = api.rune_providers()
print(f"RUNE Providers: api.rune_providers() found {len(providers)} total")
provider_detail = api.rune_provider(providers[0].rune_address)
print(f"RUNE Provider: api.rune_provider() found {provider_detail} result")
