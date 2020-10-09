import sqlite3

# შემოგვაქვს ბაზის ობეიქტი
conn = sqlite3.connect('data.db')
# ვქმნით კურსორს
cursor = conn.cursor()

params = ("Tetritskaro", "წენგოსფერი მცურავი", "1-10-2020", "არა", 1.48)

cursor.execute('INSERT INTO snake VALUES (?, ?, ?, ?, ?)', params)

# ვინახავთ (commit) ცვლილებებს
conn.commit()

# პროცესის დასრულების შემდგომ ვხურავთ კავშირს
conn.close()
