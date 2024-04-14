import csv
import sqlite3

print("Customer Data Importer")

# csv_file = input("CSV file:\t")
db_file = input("DB file:\t")
table_name = input("Table name:\t")

conn = sqlite3.connect(db_file)
c = conn.cursor()
query = "DELETE FROM ?"
c.execute(query, table_name)
conn.commit()

# with open(csv_file, "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#

conn.close()
