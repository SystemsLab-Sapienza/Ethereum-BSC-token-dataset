import argparse
from check_token import check_token


def main():
    parser = argparse.ArgumentParser(
        description="Tool to check if a smart contract is an ERC-20/BEP-20 token.")

    parser.add_argument('-b', '--blockchain', required=True,
                        choices=['ethereum', 'bsc'])

    parser.add_argument('-a', '--address', required=True)

    args = parser.parse_args()

    # Remote endpoints
    remote_provider_bsc = 'https://bscrpc.com'
    remote_provider_eth = 'https://eth.public-rpc.com'

    if args.blockchain == 'ethereum':
        check_token(remote_provider_eth, 'ERC-20', args.address)
    elif args.blockchain == 'bsc':
        check_token(remote_provider_bsc, 'BEP-20', args.address)


main()
