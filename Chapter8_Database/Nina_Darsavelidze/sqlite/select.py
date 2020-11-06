import sqlite3

conn = sqlite3.connect('data.db')

cursor = conn.cursor()

cursor.execute('SELECT breed FROM pets WHERE age=?', (4, ))

rows = cursor.fetchall()

for row in rows:
    print(row)

print(rows)

conn.close()