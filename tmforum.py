import requests


def create_product(params):
    URL = 'http://env-4126955.jelastic.servint.net/DSProductCatalog/api/productOffering'
    return get_request(URL, params)


def get_product(params):
    URL = 'http://env-4126955.jelastic.servint.net/DSProductCatalog/api/productOffering'
    return get_request(URL, params)


def create_order(params):
    URL = 'http://env-4126955.jelastic.servint.net:8080/DSProductOrdering/api/productOrder'
    return get_request(URL, params)


def get_request(URL, params):
    response = requests.get(URL, params=params)
    if response.status_code != 200:
        return None
    response = response.json()
    return response
