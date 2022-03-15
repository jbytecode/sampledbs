using SQLite
using Dates 

db = SQLite.DB("./prices.sqlite")

DBInterface.execute(db, 
"""
create table if not exists Prices 
    (date date, item text, price number)
"""
)

mydate = Date(2022,01,01)
letters = split("ABCDEFGHIJKLMNOPRSUVYZWX", "")

for i in 1:365
    for letter in letters 
        price = rand() * 100
        mystrdate = string(mydate)
        sql = "insert into Prices (date, item, price) values ('$mystrdate', '$letter', $price)"
        DBInterface.execute(db, sql)
    end
    global mydate += Dates.Day(1) 
end 


DBInterface.close!(db)

