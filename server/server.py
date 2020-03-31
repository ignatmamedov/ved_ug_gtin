from flask import Flask, jsonify
import os
import sqlite3

app = Flask(__name__)
row=['gtin', 'barcode_type', 'barcode_formats',
                   'asin', 'model',
                   'product_name','category',
                   'brand','color',
                   'description','features',
                   'images','stores','reviews']

@app.route('/kod_search/gtins/<string:gtin_id>', methods=['GET'])
def get_gtin(gtin_id):
    conn = sqlite3.connect("gtins_db.db")
    cursor = conn.cursor()
    sql = "SELECT * FROM gtins WHERE gtin=?"
    jsn_result={}
    gs_id=str(gtin_id)
    cursor.execute(sql, [gs_id])
    result=cursor.fetchall()
    result=result[0]
    for i in range(len(row)):
        jsn_result[row[i]]=result[i]
    return jsonify(jsn_result)


if __name__ == '__main__':
    app.run(debug=True)
