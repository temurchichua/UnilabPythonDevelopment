import sqlite3


connection=sqlite3.connect("bookshop.db")

cursor=connection.cursor()

data=[("Big bang theory","Steven Howking",20,2015),("My short history","Steven Howking",20,2014)]

# connection.execute("CREATE TABLE bookshop(name text,author text,price real,year integer)")
# connection.execute("INSERT INTO bookshop VALUES('Harry Potter','JK Rowling',10.54,2008)")
# connection.execute("INSERT INTO bookshop(name,year,price) VALUES('English grammar',2020,20.80)")
# connection.executemany("INSERT INTO bookshop VALUES(?,?,?,?)",data)
lista=connection.execute("SELECT * FROM bookshop WHERE author='Steven Howking'")
for i in lista:
    print(i)
# connection.commit()
