import os
from flask import Flask


app = Flask(__name__)


#Create our index or root / route
@app.route("/")
@app.route("/index")
def index():
    secret = os.environ['SECRET_PASS']
    return "This is the application mynote & I'm alive" + str(secret)

if __name__ == "__main__":
    app.run(debug="True")
