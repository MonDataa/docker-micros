from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# TODO: Use a dedicated config file or environment variables
SERVICES = {
    "checksum": "http://checksum-service:5001",
    "database": "http://database-service:5006"
}

@app.route('/')
def home():
    return jsonify({"message": "Bienvenue à l'API Gateway"}), 200

@app.route('/checksum', methods=["POST"])
def checksum():
    try:
        data = request.get_json()
        response = requests.post(f"{SERVICES['checksum']}/checksum", json=data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Erreur de communication avec le service de checksum", "details": str(e)}), 500

@app.route('/list-checksums', methods=["GET"])
def list_checksums():
    try:
        response = requests.get(f"{SERVICES['database']}/get-checksums")
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Erreur de communication avec le service de base de données", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5005)

