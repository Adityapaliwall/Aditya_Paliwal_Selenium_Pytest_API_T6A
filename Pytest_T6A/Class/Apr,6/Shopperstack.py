import requests
import urllib3

urllib3.disable_warnings()
base = "https://www.shoppersstack.com/shopping"

token = ""
UserId = ""

def add_shop():
    body = {
        "city": "zaipur",
        "country": "Ramnagar",
        "email": "zarn123@gmail.com",
        "firstName": "Why",
        "gender": "MALE",
        "lastName": "Know",
        "password": "123qwe",
        "phone": 9988776695,
        "state": "Mirzapur",
        "zoneId": "ALPHA"
            }

    response = requests.post(f"{base}/shoppers",json=body, verify=False)

    print(response.status_code)
    print(response.json())

    # assert response.status_code == 201

def user_login():
    global token, UserId
    body = {
        "email": "zarn123@gmail.com",
        "password": "123qwe",
        "role": "SHOPPER"
        }

    response = requests.post(f"{base}/users/login", json=body, verify=False)

    print(response.status_code)
    print(response.json())
    token = response.json()["data"]['jwtToken']
    UserId = response.json()["data"]['userId']
    print(f"Token value: {token}")
    print(f"User Id: {UserId}")

def get_user_info():
    header = { "Authorization": f"Bearer {token}"}
    response = requests.get(f"{base}/shoppers/{UserId}",
                headers=header, verify=False)
    print(response.status_code)
    print(response.json())


add_shop()
user_login()
get_user_info()

