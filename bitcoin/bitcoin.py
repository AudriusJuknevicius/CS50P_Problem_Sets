# https://cs50.harvard.edu/python/2022/psets/4/bitcoin/

import requests
import sys

try:
    len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
    

except requests.RequestException:
    ...
