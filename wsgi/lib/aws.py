import os
from amazon.api import AmazonAPI


class AWS(object):
    amazon_key = os.environ['amazon_key']
    amazon_secret = os.environ['amazon_secret']
    amazon_code = os.environ['amazon_code']

    amazon = AmazonAPI(amazon_key, amazon_secret, amazon_code)

    def formatify(self, product):

        product = {'storageId': product.asin,
                   'code': product.ean,
                   'name': product.title,
                   'description': ''}

        return product

    def getByEAN(self, code):
        product = self.amazon.lookup(ItemId=code,
                                     IdType='EAN',
                                     SearchIndex='All')

        if product.title:
            product = self.formatify(product)
        else:
            product = []
        return product

    def getItem(self, code):
        return self.getByEAN(code)
