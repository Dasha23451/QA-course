import requests

BASE_URL = 'http://shop.qatl.ru/api'

LIST_PRODUCTS_URI = '/products'
ADD_PRODUCT_URI = '/addproduct'
EDIT_PRODUCT_URI = '/editproduct'
DELETE_PRODUCT_URI = '/deleteproduct'

class ProductsApi:
    _METHOD_GET = 'GET'
    _METHOD_POST = 'POST'
    _ID_PARAM = 'id'

    def list(self):
        response = requests.request(
            self._METHOD_GET, BASE_URL + LIST_PRODUCTS_URI)

        return response.json()

    def add(self, product):
        response = requests.request(
            self._METHOD_POST, BASE_URL + ADD_PRODUCT_URI,
            json=product)

        try:
            return response.json()
        except:
            return {'status': 0}

    def edit(self, product):
        response = requests.request(
            self._METHOD_POST,
            BASE_URL + EDIT_PRODUCT_URI,
            json=product)

        try:
            return response.json()
        except:
            return {'status': 0}

    def delete(self, id):
        params = {self._ID_PARAM: id}

        response = requests.request(
            self._METHOD_GET,
            BASE_URL + DELETE_PRODUCT_URI,
            params=params)

        return response.json()

