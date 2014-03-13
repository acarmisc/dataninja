from flask import Flask, jsonify
from localstorage import LocalStorage


app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
__version__ = '0.1'


@app.route("/version")
def version():
    return jsonify(version=__version__)


@app.route("/item/<code>", methods=['GET'])
def getItem(code):
    res = []

    # local storage
    ls = LocalStorage()
    data = ls.getItem(code)

    r = {'source': 'LocalStorage', 'data': data}
    res.append(r)

    # amazon
    # TODO

    # ebay
    # TODO

    return jsonify({'items': res})

if __name__ == "__main__":
    app.run(debug=True)
