import sqlite3

conn = sqlite3.connect('data.db')

cursor = conn.cursor()

parameters = [(2, "Amelie", "Cat", "Female", 3, 3),
              (3, "Victoria", "Cat", "Female", 1, 3)]

# cursor.execute('INSERT INTO pets VALUES (?, ?, ?, ?, ?, ?)', parameters)

# გადავცემთ პარამეტრად ლისტს
cursor.executemany('INSERT INTO pets VALUES (?, ?, ?, ?, ?, ?)', parameters)

# გადავცემთ პარამეტრებს თანმიმდევრობის გარეშე
# cursor.executemany('INSERT INTO pets (age, weight, name, breed, _id) VALUES (?, ?, ?, ?, ?, ?)', parameters)

conn.commit()

conn.close()