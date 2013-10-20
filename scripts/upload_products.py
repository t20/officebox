import json
import csv
from pprint import pprint

from tmforum import create_product

def import_products():
    template_file = open('product_template.js')
    template = json.load(template_file)
    template_file.close()
    
    with open('products.csv', 'rb') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            template['name'] = row[0]
            template['description'] = row[1]
            template['productOfferingPrices'][0]['price']['amount'] = row[2]
            # pprint(template)
            response = create_product(template)
            print response
    
    print 'Process completed'    


if __name__ == '__main__':
    import_products()