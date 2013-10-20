import requests


def get_products(category):
    URL = ''
    response = requests.get(URL)
    if response.status_code != 200
        return None
    response = response.json()
    return response


def create_order(params):
    URL = ''
    params = {}
    response = requests.get(URL, params=params)
    if response.status_code != 200
        return None
    response = response.json()
    return response
