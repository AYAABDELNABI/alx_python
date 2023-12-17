"""
A Python script that takes your GitHub credentials (username and password) and 
uses the GitHub API to display  id

- You must use Basic Authentication with a personal access token as password to 
access to your information (only read:user permission is needed)
- The first argument will be your username
- The second argument will be your password (in your case, a personal access token as password)
"""

import requests
import sys

username = sys.argv[1]
password = sys.argv[2]


req = requests.get("https://api.github.com/user", auth= (username,password))
if req.status_code == 200:
    req_json = req.json()
    req_id = req_json["id"]
    print(req_id)
else:
    print("None")