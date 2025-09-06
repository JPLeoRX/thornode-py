from thornode_api import THORNodeAPI

api = THORNodeAPI()

print("Auth:")
print(api.accounts("thor1c2ej2t59upl2mwky9hj2y20wdst5gklyzpc4m4"))

print("Bank:")
print(api.balances("thor1c2ej2t59upl2mwky9hj2y20wdst5gklyzpc4m4"))

print("Health:")
print(api.ping())

print("Thornames:")
print(api.thorname("rapidoswaps"))

print("Pools:")
print(len(api.pools()))
print(api.pool("BTC.BTC"))

print("Derived Pools:")
print(len(api.dpools()))
print(api.dpool("THOR.BTC"))

print("Pool Slips:")
print(len(api.slips()))
print(api.slip("BTC.BTC"))



