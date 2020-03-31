import sqlite3
conn = sqlite3.connect("gtins_db.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE gtins
                  (gtin, barcode_type, barcode_formats,
                   asin, model,
                   product_name,category,
                   brand,color,
                   description,features,
                   images,stores,reviews)
               """)

cursor.execute("""INSERT INTO gtins
                  VALUES ('0886736874135', 'UPC', 'UPC 886736874135, EAN 0886736874135',
                  'B01KUHG2G8', 'CE-XL3200',
                  'Nike Red Running Shoes - Size 10', 'Apparel & Accessories > Shoes',
                  'Nike', 'Red',
                  'One of a kind, Nike Red Running Shoes that are great for walking, running and sports.',
                  'Female US 7 1/2, Mediunm',
                  'https://images.barcodelookup.com/5219/52194594-1.jpg',
                  'Newegg.com, 41.38 https://www.newegg.com/product-url ',
                  'Josh Keller, Love these shoes! A stylish and great fitting shoe for walking and running.' )"""
               )
conn.commit()
