"""
A script that starts a Flask web application:
listening on 0.0.0.0, port 5000
Routes: / display “Hello HBNB!”
"""
from flask import Flask
from flask import render_template

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
@app.route("/number_template/<int:n>")
def number_template(n):
    """
    A function that returns specifid string when routing to /number_template/<int:n>
    """
    
    return "<h1>{}</h1>".format(render_template('5-number.html', n = n))
@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    """
    A function that returns specifid string when routing to /number_odd_or_even/<int:n>
    """
    if n%2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    return render_template('6-number_odd_or_even.html', n = n, even_odd = even_odd)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port="5000")