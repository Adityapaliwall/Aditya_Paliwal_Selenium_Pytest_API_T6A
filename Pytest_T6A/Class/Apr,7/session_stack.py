import requests
import urllib3

urllib3.disable_warnings()
base = "https://www.shoppersstack.com/shopping"

session = requests.Session()

payload = {
        "email": "zarn123@gmail.com",
        "password": "123qwe",
        "role": "SHOPPER"
}

login_res = session.post(f'{base}/users/login', json=payload, verify=False)

data = login_res.json()

token = data['data']['jwtToken']
user_id = data['data']['userId']

## store token in session

session.headers.update({'Authorization': f'Bearer {token}'})

## get shoopeers

get_res = session.get(f"{base}/shoppers/{user_id}", verify=False)

print(get_res.status_code)
print(get_res.json())
