from thornode_api import THORNodeAPI

api = THORNodeAPI()

print("Bank:")
print(api.balances("thor1c2ej2t59upl2mwky9hj2y20wdst5gklyzpc4m4"))

print("Health:")
print(api.ping())

print("Thornames:")
print(api.thorname("rapidoswaps"))
