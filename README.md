# Ethereum-BSC-token-dataset

This repository contains the Token Dataset and Liquidity Pools Dataset used in the paper:

[Token Spammers, Rug Pulls, and Sniper Bots: An Analysis of the Ecosystem of Tokens in Ethereum and in the Binance Smart Chain (BNB)](https://www.usenix.org/system/files/usenixsecurity23-cernera.pdf)

Moreover, it contains a script to check whether an address is an ERC-20 (or BEP-20) compliant token and extract its information.

The full dataset contains all the ERC-20 (BEP-20) tokens and liquidity pools created on Ethereum (resp. BSC) from their inception to 2022-03-07. 
See the paper for a more detailed description of the dataset generation process.

If you use this dataset, or use the findings from the paper, please cite:

```
@inproceedings {287184,
author = {Federico Cernera and Massimo La Morgia and Alessandro Mei and Francesco Sassi},
title = {Token Spammers, Rug Pulls, and Sniper Bots: An Analysis of the Ecosystem of Tokens in Ethereum and in the Binance Smart Chain ({{{{{BNB}}}}})},
booktitle = {32nd USENIX Security Symposium (USENIX Security 23)},
year = {2023},
isbn = {978-1-939133-37-3},
address = {Anaheim, CA},
pages = {3349--3366},
url = {https://www.usenix.org/conference/usenixsecurity23/presentation/cernera},
publisher = {USENIX Association},
month = aug
}
```

## The Datasets
The dataset is divided into four files contained in the ```dataset``` folder. The ```token_dataset_eth.csv``` and ```lp_dataset_eth.csv``` contain all the data related to Ethereum,
whereas the ```token_dataset_bsc.csv``` and ```lp_dataset_bsc.csv``` contain all the data related to the BNB Smart Chain (BSC).
The files contain the same columns for Ethereum and BSC.

### The Token Dataset (```token_dataset.csv```)
Each row of this file contains:
* **address**: The address of the token
* **symbol**: The symbol of the token
* **decimals**: The decimals
* **total_supply**: The total supply of the token
* **tx_hash**: The transaction hash of the transaction where the token was created
* **from_tx**: The address that sent the creation transaction
* **creator**: The address of the smart contract used to create the token, if it was created using a smart contract
* **gas_price**: The gas price of the creation transaction
* **gas_used**: The gas used by the creation transaction
* **block_number**: The number of the block containing the token creation transaction


### The Liquidity Pool Dataset (```lp_dataset.csv```)
Each row of this file contains:
* **liquidity_token**: The address of the liquidity pool
* **address**: The address of smart contract that created the liquidity pool
* **tx_hash**: The transaction hash of the transaction where the liquidity pool was created
* **from_tx**: The address that sent the creation transaction
* **token0**: The address of one of the two tokens contained in the liquidity pool
* **token1**: The address of the other token contained in the liquidity pool
* **gas_price**: The gas price of the creation transaction
* **gas_used**: The gas used by the creation transaction
* **block_number**: The number of the block containing the liquidity pool creation transaction
  

## The Tool

Clone this repository and run:

```
pip3 install -r requirements.txt
```
To check if a token is ERC-20/BEP-20 compliant, run the ```cli.py``` script:

```
python3 cli.py -a address -b blockchain 
```

* **-a**: This argument indicates the address to check

* **-b**: This argument indicates the blockchain to consider
    
The script indicates all the ERC-20/BEP-20 functions and events implemented by the address.
Then, if it is ERC-20/BEP-20 compliant, it also provides the name, symbol, total supply, and decimal.

Two usage examples:
```
python3 cli.py -b bsc -a 0x2170Ed0880ac9A755fd29B2688956BD959F933F8
```
```
python3 cli.py -b ethereum -a 0xdAC17F958D2ee523a2206206994597C13D831ec7
```

