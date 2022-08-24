# curveFi_addLiquidity_brownie
CurveFi is an exchange liquidity pool on Ethereum (like Uniswap) designed for extremely efficient stablecoin trading

Follow the steps to run the script:
1)  Start a ganache-cli node: 
```ganache-cli —fork https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID -p XXXX```

2)  Add Brownie network: ```brownie networks add development mainnet-fork-dev cmd=ganache-cli host=http://127.0.0.1 fork='https://mainnet.infura.io/V3/YOUR_INFURA_PROJECT_ID' accounts=10 mnemonic=brownie port=XXXX```
3) Get some Weth by running: ```brownie run scripts/get_weth.py —network mainnet-fork-dev```
4) Add Liquidity by running: ```brownie run scripts/add_liquidity —network mainnet-fork-dev```

You will see the balance of the pool being increased by “amount” set to 0.5 eth atm

To be noted:
- The Curve.FI programming language is Viper: this creates some complication when you need to compile all the different contracts >> adding viper version in brownie-config.yaml helps
- To following has helpd me to navigate the different Curve Finance COntracts:
https://www.youtube.com/watch?v=0JrDbvBClEA&list=PLVOHzVzbg7bFUaOGwN0NOgkTItUAVyBBQ&index=7
