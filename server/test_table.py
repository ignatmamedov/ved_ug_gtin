import sqlite3

conn = sqlite3.connect("gtins_db.db")
cursor = conn.cursor()
sql = "SELECT * FROM gtins WHERE gtin=?"
gs_id=str('0886736874135')
cursor.execute(sql, [gs_id])
result=cursor.fetchall()
result2=result[0]
result3={}
row=['gtin', 'barcode_type', 'barcode_formats',
                   'asin', 'model',
                   'product_name','category',
                   'brand','color',
                   'description','features',
                   'images','stores','reviews']
for i  in range(len(row)):
    result3[row[i]]=result2[i]
print(result3)
