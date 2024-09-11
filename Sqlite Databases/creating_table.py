import sqlite3

conn = sqlite3.connect('class_example.sqlite')

c = conn.cursor()
query = ("CREATE TABLE IF NOT EXISTS students ("
         "id INTEGER PRIMARY KEY,"
         " first_name TEXT,"
         " last_name TEXT,"
         "age INTEGER,"
         " marks INTEGER)")

c.execute(query)
print("Table created successfully")

c.execute("""INSERT INTO students VALUES (1,'Matt', 'King', 20, 100)""")
conn.commit()
conn.close()

