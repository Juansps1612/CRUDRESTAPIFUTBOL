from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///players.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de la base de datos
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    team = db.Column(db.String(100), nullable=False)
    number = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "team": self.team,
            "number": self.number
        }

# Crear la base de datos y la tabla
with app.app_context():
    db.create_all()

# ================== Rutas ==================

# Obtener todos los jugadores
@app.route('/players', methods=['GET'])
def get_players():
    players = Player.query.all()
    return jsonify([p.to_dict() for p in players]), 200

# Obtener un jugador por ID
@app.route('/players/<int:player_id>', methods=['GET'])
def get_player(player_id):
    player = Player.query.get(player_id)
    if not player:
        return jsonify({"error": "Player not found"}), 404
    return jsonify(player.to_dict()), 200

# Crear un nuevo jugador
@app.route('/players', methods=['POST'])
def create_player():
    if not request.json or "name" not in request.json or "team" not in request.json or "number" not in request.json:
        return jsonify({"error": "Bad request"}), 400

    new_player = Player(
        name=request.json["name"],
        team=request.json["team"],
        number=request.json["number"]
    )

    db.session.add(new_player)
    db.session.commit()

    return jsonify(new_player.to_dict()), 201

# Actualizar un jugador
@app.route('/players/<int:player_id>', methods=['PUT'])
def update_player(player_id):
    player = Player.query.get(player_id)
    if not player:
        return jsonify({"error": "Player not found"}), 404

    player.name = request.json.get("name", player.name)
    player.team = request.json.get("team", player.team)
    player.number = request.json.get("number", player.number)

    db.session.commit()
    return jsonify(player.to_dict()), 200

# Eliminar un jugador
@app.route('/players/<int:player_id>', methods=['DELETE'])
def delete_player(player_id):
    player = Player.query.get(player_id)
    if not player:
        return jsonify({"error": "Player not found"}), 404

    db.session.delete(player)
    db.session.commit()
    return jsonify({"result": "Player deleted"}), 200

# ===========================================

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
