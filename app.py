from os import name
from re import search
from flask import Flask
from markupsafe import escape
from flask import request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from wtforms import form
from form import CarSearchForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'CODEX'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024),
                            nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/buy-car', methods=["GET", "POST"])
def buyCar():
    search = CarSearchForm()
    cars = Item.query.all()
    if request.method == 'POST':
        result = request.form
        return render_template('buyCarPage.html', cars=cars, search=search)
    else:
        return render_template('buyCarPage.html', cars=cars, search=search)


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


@app.route('/order/<int:order_id>')
def show_order(order_id):
    return "id is %s" % order_id


# @app.route('/result')
# def search_results(search):
#     results = []
#     search_string = search.data['search']

#     if search.data['search'] == '':
#         qry = Item.query(Album)
#         results = qry.all()


if __name__ == "__main__":
    app.run(debug=True)
