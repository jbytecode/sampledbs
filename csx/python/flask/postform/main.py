import flask
from flask import request

app = flask.Flask(__name__) 

@app.route('/')
def index():
    htmlform = """ 
    <form action="/submit" method="post">
        <input type="text" name="name" placeholder="Enter your name" value="">
        <input type="submit">
    </form>
    """
    return htmlform

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    return f'<h2>Hello {name}, <a href="/">click here to go back</a></h2>'


app.run(debug=True)
