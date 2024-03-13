import sqlite3

conn = sqlite3.connect('movie_database.sqlite')
c = conn.cursor()

movie_table = ("CREATE TABLE IF NOT EXISTS movies ("
               "Category ID integer PRIMARY key,"
               "Name text NOT NULL,"
               "Year text NOT NULL,"
               "Minutes text NOT NULL,)")

c.execute(movie_table)
conn.commit()
conn.close()
