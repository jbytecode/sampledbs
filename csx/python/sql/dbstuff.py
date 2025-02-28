import sqlite3

db = sqlite3.connect("mydatabase.db")

cur = db.cursor()

cur.execute("create table if not exists Student (id text, name text, address text)")

cur.execute("delete from Student")

cur.execute("insert into Student (id, name, address) values ('1', 'Alice', '123 Main St.')")
cur.execute("insert into Student (id, name, address) values ('2', 'Bob', '456 Elm St.')")
cur.execute("insert into Student (id, name, address) values ('3', 'Charlie', '789 Oak St.')")

db.commit()

results = cur.execute("select * from Student")

for row in results:
    print(row)

cur.execute("update Student set address = '999 Pine St.' where id = '3'")
db.commit()

results = cur.execute("select * from Student")

for row in results:
    print(row)


db.close()

