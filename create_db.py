import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Create a table named 'items' with columns 'id', 'name', and 'description'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        model TEXT
    )
''')

conn.commit()
conn.close()
