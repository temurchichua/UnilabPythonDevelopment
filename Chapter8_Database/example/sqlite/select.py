import sqlite3
#შემოგვაქვს ბაზის ობეიქტი
conn = sqlite3.connect('data.db')
# ვქმნით კურსორს
cursor = conn.cursor()

cursor.execute("SELECT breed FROM snake WHERE loc=?", ('Tbilisi',))

rows = cursor.fetchall()
print(f'მონაცემის ტიპი: {type(rows)}')
for row in rows:
    print(row)
# პროცესის დასრულების შემდგომ ვხურავთ კავშირს
conn.close()
