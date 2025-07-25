import sqlite3

conn = sqlite3.connect('inventory.db')
conn.execute('''
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    quantity INTEGER NOT NULL
)
''')
conn.close()
print("Database created!")