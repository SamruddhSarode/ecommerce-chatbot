from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def search_products(query):
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute("SELECT name, description, price FROM products WHERE name LIKE ?", ('%' + query + '%',))
    results = c.fetchall()
    conn.close()
    return results

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    if not message:
        return jsonify({'response': "Please enter a message."})

    products = search_products(message)
    if not products:
        return jsonify({'response': f"No products found for '{message}'."})

    response = "Here are some products I found:\n"
    for name, desc, price in products[:5]:
        response += f"\n🛍️ {name}\n{desc}\n💰 Price: ₹{price}\n"
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)