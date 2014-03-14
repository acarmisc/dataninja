import os
from ebaysdk.finding import Connection


class Ebay(object):
    ebay_appid = os.environ['ebay_appid']

    # siteid must be done better
    api = Connection(appid=ebay_appid, siteid='EBAY-IT')

    def formatify(self, product, code):

        product = {'storageId': product.itemId,
                   'code': code,
                   'name': product.title,
                   'description': ''}

        return product

    def getByEAN(self, code):
        products = []
        q = '<productId type="EAN">%s</productId>' % code
        self.api.execute('findItemsByProduct', q)

        res = self.api.response_obj()
        for r in res.searchResult.item:
            products.append(self.formatify(r, code))

        return products

    def getItem(self, code):
        return self.getByEAN(code)
