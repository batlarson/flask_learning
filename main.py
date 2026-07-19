from flask import Flask
from routes.activos import activos_bp

app = Flask(__name__)
app.register_blueprint(activos_bp)

if __name__ == "__main__":
    app.run(debug=True)
    