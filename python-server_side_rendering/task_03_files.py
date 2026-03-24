#!/usr/bin/python3
"""flask application for displaying Data from JSON or CSV Files in Flask"""

import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_file():
    """Read product data from the JSON file."""
    with open('products.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def read_csv_file():
    """Read product data from the CSV file."""
    product = []
    with open('products.csv', 'r', encoding='utf-8', newline='') as file:
        data = csv.DictReader(file)
        for row in data:
            product.append(
                {
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                }
            )
    return product


@app.route('/products')
def product():
    """Render product data from JSON or CSV depending on query params."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source == "json":
        product_data = read_json_file()
    elif source == "csv":
        product_data = read_csv_file()
    else:
        return render_template("product_display.html",
                               error="Wrong source", products=[])

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template("product_display.html",
                                   error="Product not found")

        filtered_products = [
            product for product in product_data
            if product["id"] == product_id
        ]

        if not filtered_products:
            return render_template(
                "product_display.html",
                error="Product not found",
                products=[]
            )

        return render_template(
            "product_display.html",
            products=filtered_products,
            error=None
        )

    return render_template(
        "product_display.html",
        products=product_data,
        error=None
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
