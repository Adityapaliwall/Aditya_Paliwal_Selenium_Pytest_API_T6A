import requests
from matplotlib.style.core import available

# response = requests.get('https://petstore.swagger.io/v2/store/inventory')
# response = requests.get('https://petstore.swagger.io/v2/pet/11223')

# expected = 200
# acutal = response.status_code
#
# assert acutal == expected
#
# print(response.text)
# print(response.status_code)
# # dict = response.json()
# # print(dict["available"])
# print(response.json()["available"])


##_______________________________________________________________________________________________________________________###
# body = {
#
#   "id": 9987,
#   "category": {
#     "id": 0,
#     "name": "string"
#   },
#   "name": "doge",
#   "photoUrls": [
#     "string"
#   ],
#   "tags": [
#     {
#       "id": 0,
#       "name": "string"
#     }
#   ],
#   "status": "available"
# }
#
# response = requests.post('https://petstore.swagger.io/v2/pet', json=body)
#
# assert response.status_code == 200
# print(response.status_code)
#
#
# archit =9987
# resp = requests.get(f'https://petstore.swagger.io/v2/pet/{9987}')
# print(resp.status_code)
# print(resp.json()["id"])

def Add_pet():
    body = {

        "id": 123,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doge",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    response = requests.post('https://petstore.swagger.io/v2/pet', json=body)
    assert response.status_code == 200
    print(response.status_code)
    # print(response.json()["id"] , "Pet Successfully registered")
    return response.json()['id']

def check_pet(p_id):
    resp = requests.get(f'https://petstore.swagger.io/v2/pet/{p_id}')
    print(resp.status_code)
    print(resp.json())
    act = resp.json()["id"]
    if(act == p_id):
        print("Pet is registered already")
    else:
        print("Pet not found")

def delete_pet(id):
    response = requests.delete(f'https://petstore.swagger.io/v2/pet/{id}')
    print(response.status_code, "Pet Successfully delted")

id = Add_pet()
check_pet(id)
delete_pet(id)