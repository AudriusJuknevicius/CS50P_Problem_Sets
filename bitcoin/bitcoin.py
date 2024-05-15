# https://cs50.harvard.edu/python/2022/psets/4/bitcoin/

import requests
import sys

# try:
#     if len(sys.argv) < 2:
#     sys.exit("Missing command-line argument")
#     elif sys.argv[2] float:
#     sys.exit("Wrong value")
#     else
# break

bitcoin_json = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

bitcoin_api = bitcoin_json.json()

for bitcoin in bitcoin_api


except requests.RequestException:
    ...
