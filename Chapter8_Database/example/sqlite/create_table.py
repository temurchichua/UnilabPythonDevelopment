import sqlite3
#შემოგვაქვს ბაზის ობეიქტი
conn = sqlite3.connect('data.db')
# ვქმნით კურსორს
cursor = conn.cursor()

# ბაზის მოდელი
# 1. snakes
# 3. loc, breed, date, venom, len
# 4. text, text, text, text, real

# ვქმნით ცხრილს
cursor.execute('CREATE TABLE snak e(loc text, breed text, date text, venom text, len real)')

cursor.execute('INSERT INTO snake VALUES ("Tbilisi", "წენგოსფერი მცურავი", "07-10-2020", "არა", 1.50)')

# ვინახავთ (commit) ცვლილებებს
conn.commit()

# პროცესის დასრულების შემდგომ ვხურავთ კავშირს
conn.close()
