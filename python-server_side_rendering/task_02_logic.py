uufrom flask import Flask, render_template
import json
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    return render_template('items.html')

file_name = f"items.json"
    try:
        with open(file_name, 'r') as f:
            content = json.load(f)
            print(content)
    except Exception as e:
        print(f"Failed to write {file_name}: {e}")
if __name__ == '__main__':
    app.run(debug=True, port=5000)
