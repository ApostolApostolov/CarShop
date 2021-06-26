from flask import Flask
from markupsafe import escape
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/buy-car')
def buyCar():
    if request.method == "POST":
        pass
    elif request.method == "GET":
        return render_template('buyCarPage.html')


@app.route('/sell-car')
def sellCar():
    if request.method == "POST":
        pass
    elif request.method == "GET":
        return 'Still in progress)'


@app.route('/about-us')
def aboutUs():
    if request.method == "GET":
        return "Still in progress"
