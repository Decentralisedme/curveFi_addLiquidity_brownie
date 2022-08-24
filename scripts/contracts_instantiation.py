from brownie import (
    AddressProvider,
    Registry,
    Tricrypto,
    Contract,
    accounts,
    network,
    config,
    interface,
)

# POOL COINS
weth_addr = config["networks"][network.show_active()]["weth_address"]
wbtc_addr = config["networks"][network.show_active()]["wbtc_address"]
usdt_addr = config["networks"][network.show_active()]["usdt_address"]


def addressProviderContract():
    address_provider_addr = config["networks"][network.show_active()][
        "address_provider_address"
    ]
    abi_add_prov = AddressProvider.abi
    address_provider_contract = Contract.from_abi(
        AddressProvider, address_provider_addr, abi_add_prov
    )
    return address_provider_contract


def registryContract():
    address_provider_contract = addressProviderContract()
    registry_addr = address_provider_contract.get_registry()
    abi_registry = Registry.abi
    registry_contract = Contract.from_abi(AddressProvider, registry_addr, abi_registry)
    return registry_contract


def poolContract():
    registry_contract = registryContract()
    pool_address = registry_contract.find_pool_for_coins(weth_addr, wbtc_addr)
    abi_tri = Tricrypto.abi
    tri_contract = Contract.from_abi(Tricrypto, pool_address, abi_tri)
    return tri_contract


def main():
    addressProviderContract()
