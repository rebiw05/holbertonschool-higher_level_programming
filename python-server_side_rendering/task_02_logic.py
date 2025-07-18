from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route("/items")
def display_items():
    items_file = os.path.join(os.path.dirname(__file__), "items.json")
    try:
        with open(items_file, "r") as f:
            data = json.load(f)
            items = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        items = []

    return render_template("items.html", items=items)

if __name__ == "__main__":
    app.run(debug=True)
