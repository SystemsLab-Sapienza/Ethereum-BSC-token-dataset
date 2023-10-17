from web3 import Web3
import json

name_f = 'name()'
symbol_f = 'symbol()'
decimal_f = 'decimals()'
totalsupply_f = 'totalSupply()'
balanceof_f = 'balanceOf(address)'
transfer_f = 'transfer(address,uint256)'
transferfrom_f = 'transferFrom(address,address,uint256)'
approve_f = 'approve(address,uint256)'
allowance_f = 'allowance(address,address)'
transfer_e = 'Transfer(address,address,uint256)'
approval_e = 'Approval(address,address,uint256)'

data_path = 'data/'


# Functions that an ERC-20 token must implement
to_implement_erc20 = [totalsupply_f, balanceof_f, transfer_f, transferfrom_f, approve_f, allowance_f, transfer_e, approval_e]

# Functions that a BEP-20 token must implement
to_implement_bep20 = to_implement_erc20 + [name_f, decimal_f]

w3 = None

with open('bep20.abi', 'r+') as out:
    contract_abi = json.load(out)


def implements(function, bytecode):
    """ Checks if the bytecode contains the kekkac-256 of the functions """
    kekkac = w3.keccak(text=function).hex()[2:10]
    return kekkac in bytecode


def check_implements_functions(functions, bytecode):
    """ Checks if the bytecode contains a list of functions """
    flag = True
    for f in functions:
        if implements(f, bytecode):
            print('The token implements {}'.format(f))
        else:
            print('The token does not implement {}'.format(f))
            flag = False
    return flag


def is_erc20(bytecode):
    """ Checks if the contract is ERC-20 compliant """
    return check_implements_functions(to_implement_erc20, bytecode)


def is_bep20(bytecode):
    """ Checks if the contract is BEP-20 compliant """
    return check_implements_functions(to_implement_bep20, bytecode)


def print_info(address, bytecode):
    """ Print the attributes of the ERC-20/BEP20 tokens  """

    # Instantiate code with the BEP-20 abi
    cont = w3.eth.contract(address=address, abi=contract_abi)

    print('### info ###')
    if implements(name_f, bytecode):
        name = cont.functions.name().call()
        print('name: {}'.format(name))
    if implements(symbol_f, bytecode):
        symbol = cont.functions.symbol().call()
        print('symbol: {}'.format(symbol))
    if implements(totalsupply_f, bytecode):
        total_supply = cont.functions.totalSupply().call()
        print('total_supply: {}'.format(total_supply))
    if implements(decimal_f, bytecode):
        decimal = cont.functions.decimals().call()
        print('decimal: {}'.format(decimal))


def check_token(remote_provider, token_type, address):
    """ Check if a smart contract is ERC-20/BEP20 compliant """
    global w3
    w3 = Web3(Web3.HTTPProvider(remote_provider))
    bytecode = w3.eth.get_code(address).hex()

    if bytecode == '0x':
        print('Contract not found or deleted.')
        return False

    check_compliant = is_erc20 if token_type == 'ERC-20' else is_bep20

    if check_compliant(bytecode):
        print('The token is {} compliant'.format(token_type))
        print_info(address, bytecode)
    else:
        print('The token is not {} compliant'.format(token_type))
