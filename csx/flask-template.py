import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    formdata = """
        <form method="post" action="getdata">
        <input type="text" placeholder = "Enter your name" name="namefield"/>
        <input type="submit"/>
        </form>
    """
    return(formdata)
  
@app.route("/getdata", methods = ["POST"])
def getdatafunction():
    name = flask.request.form["namefield"]
    return(f"Welcome {name}!")

app.run(debug=True)
