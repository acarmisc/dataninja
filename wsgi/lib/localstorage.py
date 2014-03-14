import os
import pymongo
import ConfigParser
from models.product import Product


class LocalStorage(object):

    config = ConfigParser.RawConfigParser()

    if config.read('config.ini'):
        db_url = config.get('mongodb', 'db_url')
        db_name = config.get('mongodb', 'db_name')
    else:
        db_url = os.environ['OPENSHIFT_MONGODB_DB_URL']
        db_name = os.environ['OPENSHIFT_APP_NAME']

    conn = pymongo.Connection(db_url)
    db = conn[db_name]

    def createDb(self, testname=False):
        """ TODO: function that initialize the database """

        if testname:
            db = self.conn[testname]
        else:
            db = self.db

        data = {'code': '1234567890123',
                'name': 'Test product',
                'description': 'Lorem ipsum dolor sit amet'}

        products = db.products
        pid = products.insert(data)

        return pid

    def dropDb(self, testname=False):
        if testname:
            res = self.conn.drop_database(testname)
        else:
            res = False

        return res

    def getItem(self, code):
        """ This function fetch specific item from db """
        products = []
        results = self.db.products.find({'code': code})
        for r in results:
            prod = Product(**r)
            products.append({'storageId': prod._id.__str__(),
                             'code': prod.code,
                             'name': prod.name,
                             'description': prod.description})

        return products

    def storeProduct(self, data):
        products = self.db.products
        pid = products.insert(data)

        return pid