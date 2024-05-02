import requests
import json

URL = "http://127.0.0.1:8000/customer-update/"
data = {
    'id' : 4,
    'name' : 'Team Friends JP',
    'contact' : '(+81)9072632735',
    'email' : "info@teamfriends.co.jp",
    'address' : "Nihonbashi Tomizawacho 9-4, THE E.A.S.T. 7th floor, Chuo-ku, Tokyo 103-0006, JP",
    'date_of_birth' : "2021-09-01",
}

json_data = json.dumps(data)
req = requests.put(url = URL, data=json_data)
res = req.json()
print(res)