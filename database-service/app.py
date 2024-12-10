from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Chemin de la base de données
DB_PATH = "checksums.db"

# Initialiser la base de données
def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS checksums (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            string TEXT NOT NULL,
            checksum TEXT NOT NULL
        )
    ''')
    conn.close()

init_db()

@app.route('/save-checksum', methods=['POST'])
def save_checksum():
    try:
        data = request.get_json()
        string, checksum = data.get('string'), data.get('checksum')

        if not string or not checksum:
            return jsonify({"error": "Invalid input"}), 400

        conn = sqlite3.connect(DB_PATH)
        conn.execute('INSERT INTO checksums (string, checksum) VALUES (?, ?)', (string, checksum))
        conn.commit()
        conn.close()

        return jsonify({"message": "Checksum saved"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get-checksums', methods=['GET'])
def get_checksums():
    try:
        conn = sqlite3.connect(DB_PATH)
        rows = conn.execute('SELECT * FROM checksums').fetchall()
        conn.close()

        data = [{"id": row[0], "string": row[1], "checksum": row[2]} for row in rows]
        return jsonify({"data": data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5006)

