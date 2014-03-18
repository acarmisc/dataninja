import os
import sys
from amazon.api import AmazonAPI


sys.path.append('..')
from models.product import Product


class AWS(object):
    amazon_key = os.environ['amazon_key']
    amazon_secret = os.environ['amazon_secret']
    amazon_code = os.environ['amazon_code']

    amazon = AmazonAPI(amazon_key, amazon_secret, amazon_code)

    def getByUPC(self, code):
        products = []
        try:
            product = self.amazon.lookup(ItemId=code,
                                         IdType='UPC',
                                         SearchIndex='All')
            # should return only one element
            product = Product(storageId=product.asin,
                              code=code,
                              name=product.title)
            products.append(product.__dict__)
        except:
            pass

        return products

    def getByEAN(self, code):
        products = []
        try:
            product = self.amazon.lookup(ItemId=code,
                                         IdType='EAN',
                                         SearchIndex='All')
            # should return only one element
            product = Product(storageId=product.asin,
                              code=code,
                              name=product.title)
            products.append(product.__dict__)
        except:
            pass

        return products

    def getItem(self, code, ctype=False, request=False):
        if ctype == 'UPC':
            res = self.getByUPC(code)
        else:
            res = self.getByEAN(code)

        return res
