# David Nana wrote the code for the app.py
from flask import Flask, render_template, request, redirect # type: ignore
import sqlite3

app = Flask(__name__)

# Connect to DB
def connect_db():
    return sqlite3.connect('inventory.db')

# Display inventory
@app.route('/')
def index():
    conn = connect_db()
    items = conn.execute('SELECT * FROM inventory').fetchall()
    conn.close()
    return render_template('index.html', items=items)

# Create item
@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    quantity = request.form['quantity']
    conn = connect_db()
    conn.execute('INSERT INTO inventory (name, quantity) VALUES (?, ?)', (name, quantity))
    conn.commit()
    conn.close()
    return redirect('/')

# Update item
@app.route('/update/<int:item_id>', methods=['POST'])
def update(item_id):
    quantity = request.form['quantity']
    conn = connect_db()
    conn.execute('UPDATE inventory SET quantity = ? WHERE id = ?', (quantity, item_id))
    conn.commit()
    conn.close()
    return redirect('/')

# Delete item
@app.route('/delete/<int:item_id>')
def delete(item_id):
    conn = connect_db()
    conn.execute('DELETE FROM inventory WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)