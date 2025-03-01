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
#tables created
print("Recipe tables created successfully.")


file_path = '.csv'  

with open(file_path, newline='', encoding='utf-8-sig') as recipes:
    reader = csv.DictReader(recipes)  #read as a dictionary 

    for row in reader:
        #prepare data for insertion
        recipe_id = row['id']
        recipe_name = row['recipe_name']
        instructions = row['instructions']
        notes = row['notes']
        spice = float(row['spice']) if row['spice'] else None
        temp = float(row['temp']) if row['temp'] else None
        likes = int(row['likes']) if row['likes'] else 0
        dislikes = int(row['dislikes']) if row['dislikes'] else 0
        aroma = row['aroma'] if row['aroma'] else None
        taste = row['taste'] if row['taste'] else None
        texture = row['texture'] if row['texture'] else None
        plant_based = int(row['plantBased'])
        gf = int(row['gf'])
        vegan = int(row['vegan'])
        made = int(row['made']) if row['made'] else 0
        energy = float(row['energy']) if row['energy'] else None
        cook_time = int(row['cook_time']) if row['cook_time'] else None
        prep_time = int(row['prep_time']) if row['prep_time'] else None
        servings = int(row['Servings']) if row['Servings'] else None


        # Insert data into the Recipes table
        cursor.execute('''
            INSERT INTO Recipes (
                recipe_id, recipeName, instructions, notes, spice, temp, likes, dislikes, aroma,
                taste, texture, plantBased, gf, vegan, made, energy, cookTime, prepTime, servings
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            recipe_id, recipe_name, instructions, notes, spice, temp, likes, dislikes, aroma,
            taste, texture, plant_based, gf, vegan, made, energy, cook_time, prep_time, servings
        ))
conn.commit()
conn.close()

print("Recipes inserted successfully!")

conn.commit()
conn.close()

