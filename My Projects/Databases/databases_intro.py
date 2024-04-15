# Import module
import sqlite3

# Connect to the database
conn = sqlite3.connect('guitar_shop.sqlite')

c = conn.cursor()
query = 'select * from Product '
c.execute(query)
rows = c.fetchall()
conn.close()

for row in rows:
    print(row)
