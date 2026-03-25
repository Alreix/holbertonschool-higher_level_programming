#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_file():
    with open('products.json', 'r') as file:
        return json.load(file)

def read_csv_file():
    with open('products.csv', 'r') as file:
        return list(csv.DictReader(file))

def read_sql_file():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    try:
        if source == 'json':
            products_data = read_json_file()
        elif source == 'csv':
            products_data = read_csv_file()
        elif source == 'sql':
            products_data = read_sql_file()
        else:
            return render_template(
                'product_display.html',
                error="Wrong source",
                products=[]
            )

        if product_id:
            products_data = [
                product for product in products_data
                if str(product.get('id')) == str(product_id)
            ]

            if not products_data:
                return render_template(
                    'product_display.html',
                    error="Product not found",
                    products=[]
                )

        return render_template(
            'product_display.html',
            products=products_data,
            error=None
        )
    
    except sqlite3.Error:
        return render_template(
            'product_display.html',
            error="Database error",
            products=[]
        )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
