from core.base_api import BaseAPI
from utils.config import BASE_URL


class CART_API:
    def __init__(self):
        self.api = BaseAPI(BASE_URL)

    ### post cart
    def addToCart(self, shopper_id, payload, headers):
        return self.api.post(f"/shoppers/{shopper_id}/carts", json=payload, headers=headers)

    ### get Cart
    def getToCart(self, shopper_id, headers):
        return self.api.get(f"/shoppers/{shopper_id}/carts", headers=headers)