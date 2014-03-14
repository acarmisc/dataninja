from flask import Flask, jsonify
from lib.localstorage import LocalStorage as LS
from lib.aws import AWS
from lib.ebay import Ebay
import ConfigParser

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
__version__ = '0.1'
__environ__ = 'dev'

config = ConfigParser.RawConfigParser()


@app.route("/version")
def version():
    return jsonify(version=__version__)


@app.route("/item/<code>", methods=['GET'])
def getItem(code):
    aws = AWS()
    ls = LS()
    ebay = Ebay()
    res = []

    # local storage
    found = ls.getItem(code)
    r = {'source': 'LocalStorage', 'data': found, 'size': len(found)}
    res.append(r)
    # TODO: if not found locally looking elsewhere

    # amazon
    found = aws.getItem(code)
    r = {'source': 'AWS', 'data': found, 'size': len(found)}
    res.append(r)

    # ebay
    found = ebay.getItem(code)
    r = {'source': 'Ebay', 'data': found, 'size': len(found)}
    res.append(r)

    return jsonify({'results': res})

if __name__ == "__main__":
    app.run(debug=True)
