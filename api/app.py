import os
from flask import (Flask, render_template)
from flask_restplus import Api
from mongoengine import connect
from config import *
from v1.resources.routes import initialize_routes

app = Flask(__name__)

@app.route("/")
def my_index():
    return render_template("index.html", flask_token="Hello   world")


config = globals()[os.environ['ENV']]
app.config.from_object(config)
connect('app', host=config.MONGODB_URL)

api = Api(app)

initialize_routes(api)

if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT)