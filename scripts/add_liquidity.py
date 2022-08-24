from brownie import (
    network,
    config,
    interface,
)
from scripts.helpful_scripts import get_account, approve_erc20
from scripts.contracts_instantiation import addressProviderContract, registryContract, poolContract

def main():
    account = get_account()

    weth_addr = config["networks"][network.show_active()]["weth_address"]
    wbtc_addr = config["networks"][network.show_active()]["wbtc_address"]
    usdt_addr = config["networks"][network.show_active()]["usdt_address"]

    #  Contract: AddressProvider
    address_provider_contract = addressProviderContract()
    #  Contract: Registry
    registry_contract = registryContract()
    #  Contract: Tricrypto Pool
    tri_contract = poolContract()

    # BALANCES I
    weth_int = interface.IERC20(weth_addr)
    balance_weth = weth_int.balanceOf(account.address)
    print(f"My account WETH-Balance: \n {balance_weth/(10**18)}")
    coin_index = registry_contract.get_coin_indices(tri_contract.address, weth_addr, wbtc_addr)
    weth_index=coin_index[0]
    balance_tri_pool = tri_contract.balances(weth_index)
    print(f"Curve Tricrypto Pool WETH-Balance: \n {balance_tri_pool}")

    # APPROVE WETH spending
    amount = 50000000 * (10**10)
    approve_erc20(amount, tri_contract.address, weth_addr, account)

    # ADD LIQUID
    tx_add_liquid = tri_contract.add_liquidity([0, 0, amount], 0, {"from": account})
    print(f"Weth Liquidity added via: \n {tx_add_liquid}")

    # BALANCES II
    balance_weth = weth_int.balanceOf(account.address)
    print(f"My account WETH-Balance: \n {balance_weth/(10**18)}")
    balance_tri_pool = tri_contract.balances(weth_index)
    print(f"Curve Tricrypto Pool WETH-Balance: \n {balance_tri_pool}")
