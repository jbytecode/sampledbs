using SQLite, DataFrames 

db = SQLite.DB("chinook.sqlite")

query = "SELECT * FROM Customer"

result = DBInterface.execute(db, query)

df = DataFrame(result)
