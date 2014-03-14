import os
import sys
from ebaysdk.finding import Connection


sys.path.append('..')
from models.product import Product


class Ebay(object):
    ebay_appid = os.environ['ebay_appid']

    # siteid must be done better
    api = Connection(appid=ebay_appid, siteid='EBAY-IT')

    def getByEAN(self, code):
        products = []
        q = '<productId type="EAN">%s</productId>' % code
        try:
            res = self.api.execute('findItemsByProduct', q)
            res = res.response_obj()
            for r in res.searchResult.item:
                product = Product(storageId=r.itemId,
                                  code=code,
                                  name=r.title)
                products.append(product.__dict__)
        except:
            pass

        return products

    def getItem(self, code):
        return self.getByEAN(code)
