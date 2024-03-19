import sqlite3

db = sqlite3.connect("mydatabase.db")

db.execute("create table if not exists Student (id text, name text, address text)")

db.execute("delete from Student")

db.execute("insert into Student (id, name, address) values ('1', 'Alice', '123 Main St.')")
db.execute("insert into Student (id, name, address) values ('2', 'Bob', '456 Elm St.')")
db.execute("insert into Student (id, name, address) values ('3', 'Charlie', '789 Oak St.')")


results = db.execute("select * from Student")

for row in results:
    print(row)

db.execute("update Student set address = '999 Pine St.' where id = '3'")

results = db.execute("select * from Student")

for row in results:
    print(row)


db.close()

