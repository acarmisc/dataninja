from flask import Flask, jsonify
from lib.localstorage import LocalStorage as LS
from lib.aws import AWS
from lib.ebay import Ebay
from lib.dumbo import Dumbo
from lib.outpan import Outpan
import ConfigParser

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
__version__ = '0.1'
__environ__ = 'dev'

config = ConfigParser.RawConfigParser()


@app.route("/version")
def version():
    return jsonify(version=__version__)


def buildData(source, data):
    r = {'source': source, 'data': data, 'size': len(data)}
    # TODO: store data
    # call dumbo 
    return r


@app.route("/item/<code>", methods=['GET'])
def getItem(code):
    aws = AWS()
    ls = LS()
    ebay = Ebay()
    dumbo = Dumbo()
    outpan = Outpan()

    res = []

    # local storage
    res.append(buildData('LocalStorage', ls.getItem(code)))
    # TODO: if not found locally looking elsewhere

    # external sources
    res.append(buildData('Dumbo', dumbo.getItem(code)))
    res.append(buildData('AWS', aws.getItem(code)))
    res.append(buildData('AWS-UPC', aws.getByUPC(code)))
    res.append(buildData('Ebay', ebay.getItem(code)))
    res.append(buildData('Outpan', outpan.getItem(code)))

    return jsonify({'results': res})

if __name__ == "__main__":
    app.run(debug=True)
