from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///RallyCatCupBoardInventory.db'
db = SQLAlchemy(app)

class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    itemName = db.Column(db.String(50))
    category = db.Column(db.String(50))
    quantity = db.column(db.String(50))
    kosher = db.Column(db.Boolean)
    hallal = db.Column(db.Boolean)
    vegetarian = db.Column(db.Boolean)
    vegan = db.Column(db.Boolean)
    peanuts = db.Column(db.Boolean)
    gf = db.Column(db.Boolean)
    eggs = db.Column(db.Boolean)
    fish = db.Column(db.Boolean)
    soy = db.Column(db.Boolean)
    treenuts = db.Column(db.Boolean)
    shellfish = db.Column(db.Boolean)



@app.route('/', methods = ['POST', 'GET'])
def index():
    # something was added or removed
    #if method == 'POST':
     #   pass
    items = Item.query.all()
    print(items)
    return render_template('index.html', items = items)

@app.route('/add', methods=['POST', 'GET'])
def add():
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True, port=8005)