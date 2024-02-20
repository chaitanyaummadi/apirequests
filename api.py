from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'mydatabase.db'

# Define a route for the root URL
@app.route('/')
def index():
    return 'Welcome to cars data base!'

# Helper function to connect to the database
def connect_db():
    return sqlite3.connect(DATABASE)

# CREATE operation
@app.route('/add_items', methods=['POST'])
def create_item():
    func()
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO cars (name, model) VALUES (?, ?)', (data['name'], data['model']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'cars created successfully'}), 201

# READ operation
@app.route('/get_items', methods=['GET'])
def get_all_items():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cars')
    items = cursor.fetchall()
    conn.close()
    cars_list = [{'id': item[0], 'name': item[1], 'model': item[2]} for item in items]
    return jsonify({'cars': cars_list})

# UPDATE operation
@app.route('/update_items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE cars SET name = ?, model = ? WHERE id = ?', (data['name'], data['model'], item_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'cars updated successfully'})

# DELETE operation
@app.route('/delete_items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM cars WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'cars deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
