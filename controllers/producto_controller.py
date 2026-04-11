from flask import Blueprint, render_template, request, redirect
import sqlite3

producto_bp = Blueprint("producto", __name__)

def get_connection():
    return sqlite3.connect("inventario.db")

@producto_bp.route("/productos")
def productos():
    conn = get_connection()
    productos = conn.execute("SELECT * FROM productos").fetchall()
    conn.close()
    return render_template("productos.html", productos=productos)


@producto_bp.route("/productos/agregar", methods=["POST"])
def agregar():
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    cantidad = request.form["cantidad"]

    conn = get_connection()
    conn.execute(
        "INSERT INTO productos (nombre, precio, cantidad) VALUES (?, ?, ?)",
        (nombre, precio, cantidad)
    )
    conn.commit()
    conn.close()

    return redirect("/productos")


@producto_bp.route("/productos/eliminar/<int:id>")
def eliminar(id):
    conn = get_connection()
    conn.execute("DELETE FROM productos WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return redirect("/productos")
