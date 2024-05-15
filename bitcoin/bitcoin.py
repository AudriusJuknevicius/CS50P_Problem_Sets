# https://cs50.harvard.edu/python/2022/psets/4/bitcoin/

import requests
import sys

try:
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
except requests.RequestException:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

valuetimes = float(sys.argv[1])

bitcoin_json = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
bitcoin_api = bitcoin_json.json()

usdrate = bitcoin_api["bpi"]["USD"]["rate_float"]

bitcoinvalue = valuetimes * usdrate

print(f"${bitcoinvalue:,.4f}")


