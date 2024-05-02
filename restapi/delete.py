import requests
import json

URL = "http://127.0.0.1:8000/customer-delete/"
data = {
    'id' : 1,
}

json_data = json.dumps(data)
req = requests.delete(url = URL, data=json_data)
res = req.json()
print(res)