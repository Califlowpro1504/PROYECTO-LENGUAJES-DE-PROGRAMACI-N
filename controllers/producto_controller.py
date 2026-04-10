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
    return str(productos)
