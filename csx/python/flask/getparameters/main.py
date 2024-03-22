import flask 
from flask import request

app = flask.Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    name = request.args.get('name', default = 'No name provided', type = str)
    return "<h1>Hello, {}, welcome to the Flask app!</h1>".format(name)

app.run(debug = True)

