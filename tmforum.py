import requests


def get_product(params):
    URL = 'http://env-4126955.jelastic.servint.net/DSProductCatalog/api/productOffering'
    response = requests.get(URL, params=params)
    if response.status_code != 200
        return None
    response = response.json()
    return response


def create_order(params):
    URL = 'http://env-4126955.jelastic.servint.net:8080/DSProductOrdering/api/productOrder'
    response = requests.get(URL, params=params)
    if response.status_code != 200
        return None
    response = response.json()
    return response
