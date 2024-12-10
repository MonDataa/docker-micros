from flask import Flask, request, jsonify
import hashlib
import os
import json

app = Flask(__name__)

CHECKSUM_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../chunks/checksums.json"))

def load_checksums():
    if os.path.exists(CHECKSUM_FILE):
        with open(CHECKSUM_FILE, 'r') as f:
            return json.load(f)
    return []

def save_checksums(checksums):
    with open(CHECKSUM_FILE, 'w') as f:
        json.dump(checksums, f)

def compute_checksum_value(input_string, algorithm):
    try:
        hash_func = getattr(hashlib, algorithm)
        return hash_func(input_string.encode()).hexdigest()
    except AttributeError:
        return None

@app.route('/checksum', methods=["POST"])
def compute_checksum():
    try:
        data = request.get_json()
        input_string = data.get("input_string")
        algorithm = data.get("algorithm", "sha256") 
        if not input_string:
            return jsonify({"error": "Input string is required"}), 400

        checksum = compute_checksum_value(input_string, algorithm)
        if checksum is None:
            return jsonify({"error": f"Unsupported algorithm '{algorithm}'"}), 400
        checksums = load_checksums()
        checksums.append({"input": input_string, "algorithm": algorithm, "checksum": checksum})
        save_checksums(checksums)

        return jsonify({"checksum": checksum, "algorithm": algorithm}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to list all saved checksums
@app.route('/list-checksums', methods=["GET"])
def list_checksums():
    try:
        checksums = load_checksums()
        return jsonify(checksums), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)

