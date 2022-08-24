from brownie import accounts, network, config, interface
import time


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load.id
    if network.show_active() in ["mainnet-fork-dev", "mainnet-fork-infu-dev"]:
        return accounts[0]
    if network.show_active() in config["networks"]:
        account = accounts.add(config["wallets"]["from_key"])
        return account
    return None


def approve_erc20(amount, to, erc20_address, account):
    erc20 = interface.IERC20(erc20_address)
    tx = erc20.approve(to, amount, {"from": account})
    if network.show_active() in ["mainnet-fork-dev"]:
        tx.wait(1)
    else:
        time.sleep(180)
    print("Approved spending!!!")
    return tx
