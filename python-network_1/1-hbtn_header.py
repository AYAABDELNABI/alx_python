"""
A script that takes in a URL, sends a request to the URL and displays 
the value of the variable X-Request-Id in the response header.
"""

import requests
import sys


url = sys.argv[1]
req = requests.get(url)
x_req = req.headers.get('X-Request-Id')
if x_req is not None:
        print(x_req)
else:
        print ("None")