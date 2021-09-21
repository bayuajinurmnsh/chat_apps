import sqlite3

conn = sqlite3.connect("chatApps_db")
cursor = conn.cursor()

query = "select * from tbl_users"

cursor.execute(query)

records = cursor.fetchall()
for row in records:
    print(row)

cursor.close()
