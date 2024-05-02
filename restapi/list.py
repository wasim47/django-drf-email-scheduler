import requests

ApiUrl = "http://127.0.0.1:8000/customer-list/"
res = requests.get(url=ApiUrl)
data = res.json()
print(data)
