import sqlite3

# Create a new SQLite database and inventory table
conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    quantity INTEGER NOT NULL
)
''')
conn.commit()
conn.close()
print('Database and table created successfully.')
