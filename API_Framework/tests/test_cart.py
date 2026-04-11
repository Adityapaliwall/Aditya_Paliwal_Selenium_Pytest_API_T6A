from api.cart.cart_api import CART_API
from core.auth import get_auth_data
from utils.read_data import read_json

cart_api = CART_API()

def test_ADD_TO_CART(auth_data, headers):
    data = read_json("test_data/cart.json")

    details = get_auth_data()
    shopper_id = details["shopper_id"]

    response = cart_api.addToCart(shopper_id, data, headers=headers)

    assert response.status_code == 201

    print(response.json())

def test_Get_cart(auth_data, headers):

    shopper_id = auth_data["shopper_id"]
    response = cart_api.getToCart(shopper_id, headers=headers)

    print(response.json())
    assert response.status_code == 200
