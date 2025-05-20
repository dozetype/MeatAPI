from flask import Flask, jsonify, abort, request
import sqlite3
app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('meat.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():  # put application's code here
    return "hello world"


@app.route('/meat')
def get_meat():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM meat')
    rows = cur.fetchall()
    conn.close()

    result = [dict(row) for row in rows]
    return jsonify(result)

@app.route('/meat/<int:id>')
def get_meat_index(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM meat WHERE id = ?', (id,))
    row = cur.fetchone()
    conn.close()

    if row is None:
        abort(404, description=f"Meat with ID {id} not found")

    return jsonify(dict(row))

@app.route('/meat', methods=['POST']) #need a POST request to be able to create data
def post_meat():
    conn = get_db_connection()
    cur = conn.cursor()
    name, description = request.json['name'], request.json['description']
    cur.execute("INSERT INTO meat(name, description) VALUES (?, ?)", (name, description))
    conn.commit()
    conn.close()
    return jsonify({"name": name, "description": description}), 201

@app.route('/meat/<int:id>', methods=['DELETE'])
def delete_meat(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM meat WHERE id = ?", (id,))
    row = cur.fetchone()
    if row is None:
        abort(404, description=f"Meat with ID {id} not found")

    cur.execute("DELETE FROM meat WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"id": id}), 204

if __name__ == '__main__':
    app.run()