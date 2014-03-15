import os
import sys
import json
import urllib2
import ConfigParser


sys.path.append('..')
from models.product import Product


class Dumbo(object):
    config = ConfigParser.RawConfigParser()

    if config.read('config.ini'):
        dumbo_url = config.get('dumbo', 'url') + '/products/'
    else:
        dumbo_url = os.environ['dumbo_url'] + '/products/'

    def getByEAN(self, code):
        products = []
        try:
            response = json.load(urllib2.urlopen(self.dumbo_url + code))

            product = Product(storageId=response['id'],
                              code=code,
                              name=response['name'],
                              description=response['description'])
            products.append(product.__dict__)
        except:
            pass

        return products

    def getItem(self, code):
        return self.getByEAN(code)
