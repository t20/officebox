import requests

URL = 'http://tmforum-prod.apigee.net/v1/cisco-product-category-api'
def import_data():
    response = requests.get(URL)
    if response.status_code != 200:
        return
    products = response.json()
    for product in products:
        print product['name']
    

if __name__ == '__main__':
    import_data()