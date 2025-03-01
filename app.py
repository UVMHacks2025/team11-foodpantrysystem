from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import random
from datetime import datetime, timedelta


def add_item(item):
    conn = sqlite3.connect('rally_cat.db')
    cursor = conn.cursor()
    cursor.execute('''
INSERT INTO Item (itemName, category, quantity, kosher, hallal, vegetarian, vegan, peanuts, gf, eggs, fish, soy, treenuts, shellfish)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', item)
    conn.commit()
    conn.close()

def query_items(search, filters):
    conn = sqlite3.connect('rally_cat.db')
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
     #   function call to search
    items = Item.query.all()
    print(items)
    return render_template('index.html', items = items)

@app.route('/add', methods=['POST', 'GET'])
def add():
    add_item()
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True, port=8005)