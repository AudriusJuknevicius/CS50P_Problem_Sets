# https://cs50.harvard.edu/python/2022/psets/4/bitcoin/

import requests
import sys

try:
    len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

except requests.RequestException:
    ...
