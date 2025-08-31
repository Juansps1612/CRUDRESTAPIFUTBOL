# ===============================
# 🚀 CURLs para probar la API de jugadores
# Copia y pega el comando que necesites
# ===============================

# 🔹 Crear un jugador
curl -i -X POST http://localhost:5000/players \
-H "Content-Type: application/json" \
-d '{"name": "Lionel Messi", "team": "Inter Miami", "number": 10}'

# 🔹 Crear otro jugador
curl -i -X POST http://localhost:5000/players \
-H "Content-Type: application/json" \
-d '{"name": "Cristiano Ronaldo", "team": "Al Nassr", "number": 7}'

# 🔹 Obtener todos los jugadores
curl http://localhost:5000/players

# 🔹 Obtener un jugador por ID (ejemplo: 1)
curl http://localhost:5000/players/1

# 🔹 Actualizar un jugador (ejemplo: cambiar equipo del ID 1)
curl -i -X PUT http://localhost:5000/players/1 \
-H "Content-Type: application/json" \
-d '{"team": "FC Barcelona"}'

# 🔹 Eliminar un jugador (ejemplo: ID 2)
curl -i -X DELETE http://localhost:5000/players/2
