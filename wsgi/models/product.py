"""
Model for Product is a test. 
"""

class Product(object):

    def __init__(self, storageId=None, code=None, name=None, description=None):
        self.storageId = storageId
        self.code = code
        self.name = name
        self.description = description

