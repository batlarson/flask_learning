from flask import Flask, jsonify
from routes.activos import activos_bp

app = Flask(__name__)
app.register_blueprint(activos_bp)

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Recurso no encontrado"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Error interno del servidor"}), 500

if __name__ == "__main__":
    app.run(debug=True)
    