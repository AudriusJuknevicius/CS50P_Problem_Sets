# https://cs50.harvard.edu/python/2022/psets/4/bitcoin/

import requests
import sys

try:
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
except requests.RequestException:
    sys.exit

bitcoin_json = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

bitcoin_api = bitcoin_json.json()

for bitcoin in bitcoin_api["USD"]

    bitcoinvalue = bitcoin * sys.argv[2]
        print(f"${bitcoin:,.4f}")


