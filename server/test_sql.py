import sqlite3


conn = sqlite3.connect("gtins_db.db")
cursor = conn.cursor()
sql = "SELECT * FROM gtins WHERE gtin=?"
cursor.execute(sql, ["1"])
print(cursor.fetchall())

