import sqlite3

conn = sqlite3.connect('../data.db')

cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS pets (_id INTEGER, name TEXT, breed TEXT, gender TEXT, age INTEGER, weight INTEGER)')

cursor.execute('INSERT INTO pets VALUES (1, "Creg", "Python", "Male", 4, 3)')

conn.commit()

conn.close()

