import flask 
from flask import request

app = flask.Flask(__name__)

@app.route('/')
def index():
    return '<a href="about.html">Click here to visit static html page</a>'

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)


app.run(debug=True)

# python main.py