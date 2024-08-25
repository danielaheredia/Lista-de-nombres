from flask import Flask, jsonify

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Datos de ejemplo: lista de nombres de personas
nombres = ["Ana", "Luis", "Carlos", "Marta", "Sofia"]

# Define una ruta para el endpoint que devuelve la lista de nombres
@app.route('/nombres', methods=['GET'])
def get_nombres():
    return jsonify(nombres)

# Ejecuta la aplicación en modo de desarrollo
if __name__ == '__main__':
    app.run(debug=True)

