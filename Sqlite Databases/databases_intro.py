# import the module
import sqlite3

# connecting to a database file

conn = sqlite3.connect('guitar_shop.sqlite')

c = conn.cursor()
query = ("SELECT * FROM Product "
         "WHERE listprice > 700.0 "
         "ORDER BY listprice desc")
c.execute(query)
rows = c.fetchall()
conn.close()

for row in rows:
    print(row)
