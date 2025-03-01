import sqlite3
import random
from datetime import datetime, timedelta


#connect to db
conn = sqlite3.connect('rally_cat.db')
cursor = conn.cursor()

#--------------UNCOMMENT IF NEED TO CHANGE THE TABLE SETUP----------------

cursor.execute('DROP TABLE IF EXISTS Item')
#cursor.execute('DROP TABLE IF EXISTS Batch')

#item table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Item (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    itemName TEXT NOT NULL, 
    category TEXT NOT NULL,   
    quantity INTEGER DEFAULT 0,           
    kosher BOOLEAN,   
    hallal BOOLEAN,        
    vegetarian BOOLEAN,    
    vegan BOOLEAN, 
    peanuts BOOLEAN,
    gf BOOLEAN,
    eggs BOOLEAN,
    fish BOOLEAN,
    soy BOOLEAN,
    treenuts BOOLEAN,
    shellfish BOOLEAN 
)
''')

#item batch table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Batch (
    item_batch_id INTEGER PRIMARY KEY AUTOINCREMENT,
    batch_id INTEGER,
    item_id INTEGER,
    date_of_entry TEXT,
    quantity INTEGER DEFAULT 0,
    location TEXT,
    FOREIGN KEY (item_id) REFERENCES Item(item_id)
)
''')


conn.commit()
#tables created



import sqlite3
import random
from datetime import datetime, timedelta

# Connect to database
conn = sqlite3.connect('rally_cat.db')
cursor = conn.cursor()

# Insert fake data into Item table
items = [
    ("Rice", "Grains", 50, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0),
    ("Pasta", "Grains", 40, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0),
    ("Peanut Butter", "Spreads", 30, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0),
    ("Canned Tuna", "Canned Goods", 20, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0),
    ("Almonds", "Nuts", 25, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0),
    ("Milk", "Dairy", 15, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0),
    ("Eggs", "Dairy", 30, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0),
    ("Soy Milk", "Dairy Alternatives", 10, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0),
    ("Bread", "Bakery", 20, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0),
    ("Chicken Breast", "Meat", 25, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0),
    ("Tofu", "Protein", 18, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0),
    ("Lentils", "Legumes", 22, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0),
    ("Canned Beans", "Canned Goods", 28, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0),
    ("Yogurt", "Dairy", 12, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0),
    ("Chocolate", "Snacks", 16, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0),
    ("Granola Bars", "Snacks", 30, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0),
    ("Tomato Sauce", "Condiments", 14, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0),
    ("Apples", "Fruits", 35, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0),
    ("Carrots", "Vegetables", 40, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0),
    ("Orange Juice", "Beverages", 18, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0)
]

cursor.executemany('''
INSERT INTO Item (itemName, category, quantity, kosher, hallal, vegetarian, vegan, peanuts, gf, eggs, fish, soy, treenuts, shellfish)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', items)

conn.commit()

# Insert fake data into Batch table
batch_entries = []
for i in range(1, 21):
    batch_id = random.randint(1000, 9999)
    item_id = i
    date_of_entry = (datetime.now() - timedelta(days=random.randint(1, 100))).strftime("%Y-%m-%d")
    quantity = random.randint(5, 50)
    location = random.choice(["Shelf A", "Shelf B", "Freezer", "Refrigerator", "Back Storage"])
    batch_entries.append((batch_id, item_id, date_of_entry, quantity, location))

cursor.executemany('''
INSERT INTO Batch (batch_id, item_id, date_of_entry, quantity, location)
VALUES (?, ?, ?, ?, ?)
''', batch_entries)

conn.commit()

print("Fake data inserted successfully.")
conn.close()

