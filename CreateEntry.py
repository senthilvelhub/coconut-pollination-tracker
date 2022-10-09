import sqlite3

conn = sqlite3.connect('tree.db')

c = conn.cursor()

# c.execute("""
#         INSERT INTO trees VALUES (5,2,1,15,270)
#         """)

c.execute("""INSERT INTO trees VALUES(35, 76, 1, 20, 270) """)

conn.commit()

conn.close()
