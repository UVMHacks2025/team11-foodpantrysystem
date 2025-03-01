from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rally_cat.db'
db = SQLAlchemy(app)

class Item(db.Model):
    __tablename__ = "Item"
    item_id = db.Column(db.Integer, primary_key=True)
    itemName = db.Column(db.String(50))
    category = db.Column(db.String(50))
    quantity = db.Column(db.String(50))
    kosher = db.Column(db.Integer)
    hallal = db.Column(db.Integer)
    vegetarian = db.Column(db.Integer)
    vegan = db.Column(db.Integer)
    peanuts = db.Column(db.Integer)
    gf = db.Column(db.Integer)
    eggs = db.Column(db.Integer)
    fish = db.Column(db.Integer)
    soy = db.Column(db.Integer)
    treenuts = db.Column(db.Integer)
    shellfish = db.Column(db.Integer)

    def __repr__(self):
        return f'<Item {self.itemName}>'
    
#with app.app_context():
    #db.create_all()

@app.route('/', methods = ['POST', 'GET'])
def index():
    #something was added or removed
    if request.method == 'POST':
        pass
    items = Item.query.all()
    print(items)
    return render_template('index.html')

@app.route('/add', methods=['POST', 'GET'])
def add():
    return render_template('add.html')



if __name__ == "__main__":
    app.run(debug=True, port=8005)