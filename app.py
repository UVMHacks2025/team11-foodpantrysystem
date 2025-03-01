from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import random
from datetime import datetime, timedelta


def add_item(item):
    conn = sqlite3.connect('RallyCatCupboardInventory.db')
    cursor = conn.cursor()
    cursor.execute('''
INSERT INTO Item (itemName, category, quantity, kosher, hallal, vegetarian, vegan, peanuts, gf, eggs, fish, soy, treenuts, shellfish)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', item)
    conn.commit()
    conn.close()

def query_items(search, filters):
    conn = sqlite3.connect('RallyCatCupboardInventory.db')
    cursor = conn.cursor()
    
    #base query
    query = "SELECT item_id, itemName, category, quantity FROM Item WHERE 1=1"
    params = []
    
    #add search text
    if search:
        query += " AND itemName LIKE ?"
        params.append(f"%{search}%")
    
    #add filter conditions
    for filter_key in filters:
        query += f" AND {filter_key} = 1"
    
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()

    return results


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
    add_item()
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True, port=8005)