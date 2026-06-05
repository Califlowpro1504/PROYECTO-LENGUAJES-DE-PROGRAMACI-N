from flask import Flask
from controllers.producto_controller import producto_bp
import database

app = Flask(__name__)

app.register_blueprint(producto_bp)

@app.route("/")
def inicio():
    return "Sistema Inventario Activo"

if __name__ == "__main__":
    app.run(debug=True)
