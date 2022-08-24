from brownie import interface, network, config
from scripts.helpful_scripts import get_account


def get_weth():
    """
    Mints WETH by depositing ETH
    """
    amount = 5 * 10**18
    # Using Interface:
    # ABI
    # Address
    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_address"])
    tx = weth.deposit(({"from": account, "value": amount}))
    print(f"Recived {amount/10**18} WETH!!!")
    print(f"My Weth Balance: \n {weth.balanceOf(account.address)/(10**18)} ")
    return tx


def main():
    get_weth()
