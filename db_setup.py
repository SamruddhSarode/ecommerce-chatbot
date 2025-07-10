import sqlite3

conn = sqlite3.connect('products.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT,
    price REAL
)
''')

for i in range(1, 101):
    c.execute("INSERT INTO products (name, description, price) VALUES (?, ?, ?)", 
              (f"Product {i}", f"This is the description for Product {i}", round(10 + i * 1.5, 2)))

conn.commit()
conn.close()
print("Database created with 100 products.")