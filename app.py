from flask import Flask, jsonify

app = Flask(__name__)

# Simuler une base de données d'utilisateurs
# Commentaire ajouter pour vérifier le build pour une autre branche
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

@app.route('/')
def home():
    return "Bienvenue sur l'API Utilisateurs!"

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
