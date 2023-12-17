"""
A Python script that takes in a URL, sends a request to the URL and displays
the body of the response.

If the HTTP status code is greater than or equal to 400, print: 
Error code: followed by the value of the HTTP status code
"""
import requests
import sys

url = sys.argv[1]

req = requests.get(url)
req_status_code = req.status_code
if req_status_code >= 400:
    print("Error code:", req_status_code)
else:
    print("Regular request")