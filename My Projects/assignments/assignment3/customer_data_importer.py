import csv
import sqlite3

print("Customer Data Importer\n")

csv_file = input("CSV file:\t")
db_file = input("DB file:\t")
table_name = input("Table name:\t")

conn = sqlite3.connect(db_file)
c = conn.cursor()
query = "DELETE FROM {}".format(table_name)
c.execute(query)
conn.commit()

print(f"\nAll old rows deleted from {table_name} table.")
input("")

count = 0
with open(csv_file, "r") as file:
    reader = csv.reader(file)
    next(reader)
    for i, row in enumerate(reader):
        query = f"INSERT INTO {table_name} VALUES ('{101 + i}', '{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}', '{row[6]}')"
        c.execute(query)
        conn.commit()
        count += 1

print(f"{count} row(s) inserted into {table_name} table.")

conn.close()
