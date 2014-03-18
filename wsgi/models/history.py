import sys
import datetime


sys.path.append('..')
from lib.localstorage import LocalStorage as LS


class History(object):
    """
    This model describe how to log query event on LocalStorage
    """

    def __init__(self, request=None, code=None, action=None, data=None):
        #import pdb; pdb.set_trace()
        if request:
            self.client_addr = request.remote_addr
        self.timestamp = datetime.datetime.utcnow()
        self.code = code
        self.action = action
        self.data = data

    def find(self):
        ls = LS()
        return ls.getHistory()

    def save(self):
        ls = LS()
        try:
            ls.writeHistory(self)
        except:
            pass
