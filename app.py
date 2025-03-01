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

def query_items(search):
    conn = sqlite3.connect('Instance/rally_cat.db')
    cursor = conn.cursor()
    
    #base query
    query = "SELECT item_id, itemName, category, quantity FROM Item WHERE 1=1"
    params = []
    
    #add search text
    if search:
        query += " AND itemName LIKE ?"
        params.append(f"%{search}%")
    
    #add filter conditions

    #for filter_key in filters:
    #    query += f" AND {filter_key} = 1"
    
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
    
with app.app_context():
    db.create_all()

@app.route('/', methods = ['POST', 'GET'])
def index():
    # something was added or removed
    if request.method == 'POST':
        print("post")
        search = request.form['site-search']

        remove = request.form
        results = Item.query.filter_by(itemName = search).all()
        print(results)
        return render_template('index.html', items = results)
    items = Item.query.all()
    print(items)
    return render_template('index.html', items = items)

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        item_name = request.form['itemName']
        category = request.form['category']
        quantity = int(request.form['quantity'])

        #convert checkboxes to binary
        kosher = int('kosher' in request.form)
        hallal = int('hallal' in request.form)
        vegetarian = int('vegetarian' in request.form)
        vegan = int('vegan' in request.form)
        peanuts = int('peanuts' in request.form)
        gf = int('gf' in request.form)
        eggs = int('eggs' in request.form)
        fish = int('fish' in request.form)
        soy = int('soy' in request.form)
        treenuts = int('treenuts' in request.form)
        shellfish = int('shellfish' in request.form)

        #check for duplicates
        existing_item = Item.query.filter_by(itemName=item_name).first()
        if existing_item:
            return render_template('add.html', message="Item already exists!")

        #add item
        new_item = Item(
            itemName=item_name,
            category=category,
            quantity=quantity,
            kosher=kosher,
            hallal=hallal,
            vegetarian=vegetarian,
            vegan=vegan,
            peanuts=peanuts,
            gf=gf,
            eggs=eggs,
            fish=fish,
            soy=soy,
            treenuts=treenuts,
            shellfish=shellfish
        )
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/plus/<int:id>', methods = ['POST', 'GET'])
def plus(id):
    plus = request.form['plus']
    item = Item.query.get(id)
    item.quantity += 1
    db.session.commit()
    return redirect("/")
    
@app.route('/minus/<int:id>', methods = ['POST', 'GET'])
def minus(id):
    minus = request.form['minus']
    item = Item.query.get(id)
    if item.quantity > 0:
        item.quantity -= 1
        db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=8005)