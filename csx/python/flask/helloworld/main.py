import flask 

app = flask.Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'


app.run(debug=True)

