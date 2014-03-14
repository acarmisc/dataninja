import sys
import unittest
import random


sys.path.append('..')
import dataninja
from lib.localstorage import LocalStorage as LS
from lib.aws import AWS


class DataninjaTest(unittest.TestCase):

    # making test names
    db_testname = "dataninja_"
    db_testname += str(random.randint(1000, 9999))

    def setUp(self):
        self.app = dataninja.app.test_client()

    # common tests
    def test_version(self):
        """ Testing basic call that get current app version """
        res = self.app.get('/version')

        assert res.status_code == 200

    def test_getItem(self):
        """ Testing getItem function with false data """
        res = self.app.get('/item/9788817169547')

        assert "9788817169547" in res.data

    # testing localstorage
    def test_createDb(self):
        """ Testing the database creation """
        ls = LS()
        pid = ls.createDb(self.db_testname)

        assert pid

    def test_getItemDb(self):
        """ Testing item fetch from temp db """
        ls = LS()
        res = ls.getItem('9788817169547')

        assert len(res) > 0

    def test_dropDb(self):
        """ Testing the database dropping """
        ls = LS()
        ls.dropDb(self.db_testname)

        assert True

    # testing amazonstorage
    def test_getItemByEAN(self):
        """ Testing getting item by EAN code """
        aws = AWS()
        data = aws.getByEAN('9788817169547')

        assert data

if __name__ == '__main__':
    unittest.main()
