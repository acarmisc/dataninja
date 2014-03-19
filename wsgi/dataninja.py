from flask import Flask, jsonify, request
from lib.localstorage import LocalStorage as LS
from lib.aws import AWS
from lib.ebay import Ebay
from lib.dumbo import Dumbo
from lib.outpan import Outpan
from models.history import History
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

    return r


@app.route("/item/<code>", methods=['GET'])
def getAllSources(code):
    aws = AWS()
    ls = LS()
    ebay = Ebay()
    dumbo = Dumbo()
    outpan = Outpan()

    res = []

    res.append(buildData('LocalStorage', ls.getItem(code)))

    res.append(buildData('Dumbo', dumbo.getItem(code)))
    res.append(buildData('AWS', aws.getItem(code, request=request)))
    res.append(buildData('AWS-UPC', aws.getItem(code, 'UPC', request=request)))
    res.append(buildData('Ebay', ebay.getItem(code)))
    res.append(buildData('Outpan', outpan.getItem(code)))

    # saving query to db
    data = {'found': len(res)}
    History(request, code=code, action='getAllSources', data=data).save()

    return jsonify({'results': res})


@app.route("/history", methods=['GET'])
def getHistory():
    h = History()
    res = []
    els = h.find()

    for el in els:
        #import pdb; pdb.set_trace()
        res.append({'code': el['code'],
                    'action': el['action'],
                    'client_addr': el['client_addr'],
                    'timestamp': el['timestamp']})

    return jsonify({'results': res})


if __name__ == "__main__":
    app.run(debug=True)
