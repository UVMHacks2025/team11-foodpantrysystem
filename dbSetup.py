import sqlite3
import csv
import chardet


#connect to db
conn = sqlite3.connect('RallyCatCupbaordInventory.db')
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
conn.close()
print("Recipe tables created successfully.")

