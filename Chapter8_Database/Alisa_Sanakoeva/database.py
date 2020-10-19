import sqlite3

conn = sqlite3.connect('mydata.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE snakes (სახეობა text, ლოკაცია text, თარიღი text, სიგრძე real)')

data = [('წენგოსფერი მცურავი', 'ბორჯომი', '28/07/2017', 120),
        ('ხვლიკიჭამია გველი', 'ჭაჭუნა', '13/05/2018', 60),
        ('კავკასიური გველგესლა', 'ტაშისკარი', '07/06/2019', 40),
        ('წენგოსფერი მცურავი', 'თბილისი', '29/04/2016', 55)]

cursor.executemany('INSERT INTO snakes VALUES (?, ?, ?, ?)', data)

conn.commit()

cursor.execute('SELECT * FROM snakes WHERE სახეობა=?', ('წენგოსფერი მცურავი', ))

rows = cursor.fetchall()

for item in rows:
    print(item)


conn.close()


