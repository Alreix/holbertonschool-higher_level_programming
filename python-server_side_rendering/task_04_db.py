#!/usr/bin/python3
"""Flask application displaying products from JSON, CSV, or SQLite."""

import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_file():
    """Read product data from the JSON file."""
    with open('products.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def read_csv_file():
    """Read product data from the CSV file."""
    products = []
    with open('products.csv', 'r', encoding='utf-8', newline='') as file:
        data = csv.DictReader(file)
        for row in data:
            products.append(
                {
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                }
            )
    return products


def read_sql_db():
    """Read product data from the SQLite database."""
    products = []
    connexion = sqlite3.connect('products.db')
    cursor = connexion.cursor()

    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    connexion.close()

    for row in rows:
        products.append(
            {
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            }
        )
    return products


@app.route('/products')
def products():
    """Render product data from JSON, CSV, or SQLite."""
    source = request.args.get("source")

    try:
        if source == "json":
            product_data = read_json_file()
        elif source == "csv":
            product_data = read_csv_file()
        elif source == "sql":
            product_data = read_sql_db()
        else:
            return render_template(
                "product_display.html",
                error="Wrong source",
                products=[]
            )

        return render_template(
            "product_display.html",
            error=None,
            products=product_data
        )

    except sqlite3.Error:
        return render_template(
            "product_display.html",
            error="Database error",
            products=[]
        )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
