import os
import sys
import json
import urllib2
import ConfigParser


sys.path.append('..')
from models.product import Product


class Outpan(object):
    config = ConfigParser.RawConfigParser()

    if config.read('config.ini'):
        url = config.get('outpan', 'url')
    else:
        url = os.environ['outpan_url']

    def getByEAN(self, code):
        products = []
        try:
            response = json.load(urllib2.urlopen(self.url + code))

            product = Product(storageId=response['barcode'],
                              code=code,
                              name=response['name'],
                              description=response['description'])
            products.append(product.__dict__)
        except:
            pass

        return products

    def getItem(self, code):
        return self.getByEAN(code)
