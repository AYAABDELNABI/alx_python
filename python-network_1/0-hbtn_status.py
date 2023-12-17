"""
A Python script that fetches https://alu-intranet.hbtn.io/status
- type: <class 'str'>
- content: OK
"""
import requests

req = requests.get("https://alu-intranet.hbtn.io/status")
req_type = type(req.text)
req_content = req.text
print("Body response:")
print("\t- type:", req_type)
print("\t- content:",req_content)