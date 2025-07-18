from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

def read_json(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except:
        return []

def read_csv(filepath):
    products = []
    try:
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row['id']),
                    "name": row['name'],
                    "category": row['category'],
                    "price": float(row['price'])
                })
    except:
        pass
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    json_path = os.path.join(os.path.dirname(__file__), 'products.json')
    csv_path = os.path.join(os.path.dirname(__file__), 'products.csv')

    if source == 'json':
        data = read_json(json_path)
    elif source == 'csv':
        data = read_csv(csv_path)
    else:
        return render_template("product_display.html", error="Wrong source", products=None)

    if product_id:
        filtered = [item for item in data if item["id"] == product_id]
        if not filtered:
            return render_template("product_display.html", error="Product not found", products=None)
        return render_template("product_display.html", products=filtered)

    return render_template("product_display.html", products=data)

if __name__ == "__main__":
    app.run(debug=True)

