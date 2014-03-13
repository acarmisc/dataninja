import sys
import unittest
import random


sys.path.append('..')
import dataninja
from localstorage import LocalStorage


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
        res = self.app.get('/item/1234567890123')

        assert "1234567890123" in res.data

    # testing localstore
    def test_createDb(self):
        """ Testing the database creation """
        ls = LocalStorage()
        pid = ls.createDb(self.db_testname)

        assert pid

    def test_getItemDb(self):
        """ Testing item fetch from temp db """
        ls = LocalStorage()
        res = ls.getItem('1234567890123')

        assert len(res) > 0

    def test_dropDb(self):
        """ Testing the database dropping """
        ls = LocalStorage()
        ls.dropDb(self.db_testname)

        assert True


if __name__ == '__main__':
    unittest.main()
