from thornode_api import THORNodeAPI

api = THORNodeAPI()
#
# print("Auth:")
# print(api.accounts("thor1c2ej2t59upl2mwky9hj2y20wdst5gklyzpc4m4"))
#
# print("Bank:")
# print(api.balances("thor1c2ej2t59upl2mwky9hj2y20wdst5gklyzpc4m4"))
#
# print("Health:")
# print(api.ping())
#
# print("Thornames:")
# print(api.thorname("rapidoswaps"))
#
# print("Pools:")
# print(len(api.pools()))
# print(api.pool("BTC.BTC"))
#
# print("Derived Pools:")
# print(len(api.dpools()))
# print(api.dpool("THOR.BTC"))
#
# print("Pool Slips:")
# print(len(api.slips()))
# print(api.slip("BTC.BTC"))
#
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


# Nodes
nodes = api.nodes()
print(f"Nodes: api.nodes() found {len(nodes)} validators")
node_info = api.node(nodes[0].node_address)
print(f"Node: api.node() fetched node with address {node_info.node_address} and status {node_info.status}")
