import json
import requests


def create_product(params):
    URL = 'http://env-4126955.jelastic.servint.net/DSProductCatalog/api/productOffering'
    return post_request(URL, params)


def get_product(params):
    URL = 'http://env-4126955.jelastic.servint.net/DSProductCatalog/api/productOffering'
    return get_request(URL, params)


def create_order(params):
    URL = 'http://env-4126955.jelastic.servint.net:8080/DSProductOrdering/api/productOrder'
    template_file = open('order_template.js')
    template = json.load(template_file)
    template_file.close()
    return post_request(URL, template)


def post_request(URL, params):
    headers = {'content-type': 'application/json'}
    response = requests.post(URL, data=json.dumps(params), headers=headers)
    if response.status_code != 200:
        return None
    response = response.json()
    return response


def get_request(URL, params):
    response = requests.post(URL, params=params)
    if response.status_code != 200:
        return None
    response = response.json()
    return response
