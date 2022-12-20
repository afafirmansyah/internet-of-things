import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("SELECT sensor, nilai, tanggal, waktu FROM iot")
rows = cursor.fetchall()
for row in rows:
    print(row[0], row[1], row[2], row[3])
    
cursor.close()
conn.close()