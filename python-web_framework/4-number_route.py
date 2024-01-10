"""
A script that starts a Flask web application:
listening on 0.0.0.0, port 5000
Routes: / display “Hello HBNB!”
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_HBNB():
    """
    A function that returns specified string when routing to /
    """
    return "Hello HBNB!"

@app.route("/hbnb")
def hbnb():
    """
    A function that returns specifid string when routing to /hbnb
    """
    return "HBNB"

@app.route("/c/<text>")
def c_text(text):
    """
    A function that returns specifid string when routing to /c/<Text>
    """
    for _ in text:
        text = text.replace("_"," ")
        
    return "C {}".format(text)
@app.route("/python/<text>")
@app.route("/python/")
def python_text(text = "is cool"):
    """
    A function that returns specifid string when routing to /python/<Text>
    """
    for _ in text:
        text = text.replace("_"," ")
        
    return "Python {}".format(text)
@app.route("/number/<int:n>")
def python_number(n):
    """
    A function that returns specifid string when routing to /number/<n>
    """
    
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port="5000")