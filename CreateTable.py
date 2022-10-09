import sqlite3

conn = sqlite3.connect('tree.db')

c = conn.cursor()

try:
    c.execute(""" CREATE TABLE trees(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        serial_number INTEGER,
        variety INTEGER,
        min_flower_time INTEGER,
        nut_growth_time INTEGER)""")
except:
    pass

conn.commit()

conn.close()
