from flask import Flask, jsonify
from routes.usuarios import usuarios_bp

app = Flask(__name__)

# Registrar el blueprint de usuarios
app.register_blueprint(usuarios_bp, url_prefix='/api')

# Endpoint para manejo de errores 404
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"message": "Endpoint not found"}), 404

if __name__ == '__main__':
    app.run(port=5000)