from flask import Blueprint, jsonify, request

activos_bp = Blueprint('activos', __name__)

activos = [
    {"ticker": "KO", "nombre": "Coca Cola"},
    {"ticker": "ABBV", "nombre": "AbbVie"}
]

@activos_bp.route("/activos")
def listar_activos():
    return jsonify(activos)

@activos_bp.route("/activos", methods=["POST"])
def crear_activo():
    data = request.get_json()
    activos.append(data)
    return jsonify(data), 201

@activos_bp.route("/activos/<ticker>", methods=["PUT"])
def actualizar_activo(ticker):
    data = request.get_json()
    for a in activos:
        if a['ticker'] == ticker:
            a.update(data)
            return jsonify(a)
    return jsonify({"error": "No encontrado"}), 404


@activos_bp.route("/activos/<ticker>", methods=["DELETE"])
def eliminar_activo(ticker):
    global activos
    for a in activos:
        if a["ticker"] == ticker:
            activos.remove(a)
            return jsonify({"mensaje": f"{ticker} borrado"})
    return jsonify({"error": "No encontrado"}), 404