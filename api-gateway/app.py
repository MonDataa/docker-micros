from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Configuration des microservices
SERVICES = {
    "checksum": "http://checksum-service:5001",
    "database": "http://database-service:5006"
}

@app.route('/')
def home():
    """Point d'entrée de l'API Gateway."""
    return jsonify({"message": "Bienvenue à l'API Gateway"}), 200

@app.route('/checksum', methods=["POST"])
def checksum():
    """Redirige les requêtes pour calculer le checksum vers le service de checksum."""
    try:
        data = request.get_json()
        response = requests.post(f"{SERVICES['checksum']}/checksum", json=data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Erreur de communication avec le service de checksum", "details": str(e)}), 500

@app.route('/list-checksums', methods=["GET"])
def list_checksums():
    """Redirige les requêtes pour lister les checksums vers le service de base de données."""
    try:
        response = requests.get(f"{SERVICES['database']}/get-checksums")
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Erreur de communication avec le service de base de données", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5005)

