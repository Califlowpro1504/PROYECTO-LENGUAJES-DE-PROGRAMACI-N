from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db():
    return sqlite3.connect("database.db")

# ======================
# INIT DB
# ======================
def init_db():
    db = get_db()
    cursor = db.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT,
        cantidad INTEGER,
        precio REAL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo_identificacion TEXT,
        identificacion TEXT,
        nombre TEXT,
        apellido TEXT,
        numero_Telefonico TEXT,
        email TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS ventas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        producto_id INTEGER,
        cliente_id INTEGER,
        cantidad INTEGER,
        fecha TEXT,
        total REAL
    )''')

    db.commit()
    db.close()

# ======================
# INICIO
# ======================
@app.route("/")
def inicio():
    db = get_db()
    cursor = db.cursor()

    total_productos = cursor.execute("SELECT COUNT(*) FROM productos").fetchone()[0]
    total_clientes = cursor.execute("SELECT COUNT(*) FROM clientes").fetchone()[0]
    total_ventas = cursor.execute("SELECT COUNT(*) FROM ventas").fetchone()[0]
    total_ingresos = cursor.execute("SELECT IFNULL(SUM(total),0) FROM ventas").fetchone()[0]

    db.close()

    return render_template("index.html",
                           total_productos=total_productos,
                           total_clientes=total_clientes,
                           total_ventas=total_ventas,
                           total_ingresos=total_ingresos)

# ======================
# PRODUCTOS
# ======================
@app.route("/productos", methods=["GET","POST"])
def ver_productos():
    db = get_db()
    cursor = db.cursor()

    if request.method == "POST":
        cursor.execute("INSERT INTO productos(tipo,cantidad,precio) VALUES(?,?,?)",
                       (request.form["tipo"], request.form["cantidad"], request.form["precio"]))
        db.commit()
        return redirect(url_for("ver_productos"))

    productos = cursor.execute("SELECT * FROM productos").fetchall()
    db.close()

    return render_template("productos.html", productos=productos)

@app.route("/productos/<int:id>/editar", methods=["GET", "POST"])
def editar_producto(id):
    db = get_db()
    cursor = db.cursor()

    if request.method == "POST":
        cursor.execute(
            "UPDATE productos SET tipo=?, cantidad=?, precio=? WHERE id=?",
            (request.form["tipo"], request.form["cantidad"], request.form["precio"], id)
        )
        db.commit()
        db.close()
        return redirect(url_for("ver_productos"))

    producto = cursor.execute("SELECT * FROM productos WHERE id=?", (id,)).fetchone()
    db.close()

    if not producto:
        return redirect(url_for("ver_productos"))

    return render_template("editar_producto.html", producto=producto)

@app.route("/productos/<int:id>/eliminar", methods=["POST"])
def eliminar_producto(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM productos WHERE id=?", (id,))
    db.commit()
    db.close()
    return redirect(url_for("ver_productos"))

# ======================
# CLIENTES
# ======================
@app.route("/clientes", methods=["GET","POST"])
def ver_clientes():
    db = get_db()
    cursor = db.cursor()

    if request.method == "POST":
        cursor.execute("""INSERT INTO clientes(tipo_identificacion,identificacion,nombre,apellido,numero_Telefonico,email)
                          VALUES(?,?,?,?,?,?)""",
                       (request.form["tipo_identificacion"],
                        request.form["identificacion"],
                        request.form["nombre"],
                        request.form["apellido"],
                        request.form["numero_Telefonico"],
                        request.form["email"]))
        db.commit()
        return redirect(url_for("ver_clientes"))

    clientes = cursor.execute("SELECT * FROM clientes").fetchall()
    db.close()

    return render_template("clientes.html", clientes=clientes)

@app.route("/clientes/<int:id>/editar", methods=["GET", "POST"])
def editar_cliente(id):
    db = get_db()
    cursor = db.cursor()

    if request.method == "POST":
        cursor.execute(
            """UPDATE clientes
               SET tipo_identificacion=?, identificacion=?, nombre=?,
                   apellido=?, numero_Telefonico=?, email=?
               WHERE id=?""",
            (request.form["tipo_identificacion"],
             request.form["identificacion"],
             request.form["nombre"],
             request.form["apellido"],
             request.form["numero_Telefonico"],
             request.form["email"],
             id)
        )
        db.commit()
        db.close()
        return redirect(url_for("ver_clientes"))

    cliente = cursor.execute("SELECT * FROM clientes WHERE id=?", (id,)).fetchone()
    db.close()

    if not cliente:
        return redirect(url_for("ver_clientes"))

    return render_template("editar_cliente.html", cliente=cliente)

@app.route("/clientes/<int:id>/eliminar", methods=["POST"])
def eliminar_cliente(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM clientes WHERE id=?", (id,))
    db.commit()
    db.close()
    return redirect(url_for("ver_clientes"))

# ======================
# VENTAS
# ======================
@app.route("/ventas", methods=["GET","POST"])
def ver_ventas():
    db = get_db()
    cursor = db.cursor()

    if request.method == "POST":
        producto_id = request.form["id_producto"]
        cliente_id = request.form["id_cliente"]
        cantidad = int(request.form["cantidad"])

        producto = cursor.execute("SELECT * FROM productos WHERE id=?", (producto_id,)).fetchone()
        if producto:
            total = producto[3] * cantidad
            nueva_cantidad = producto[2] - cantidad

            cursor.execute("UPDATE productos SET cantidad=? WHERE id=?", (nueva_cantidad, producto_id))
            cursor.execute("INSERT INTO ventas(producto_id,cliente_id,cantidad,fecha,total) VALUES(?,?,?,?,?)",
                           (producto_id, cliente_id, cantidad, datetime.now(), total))
            db.commit()

        return redirect(url_for("ver_ventas"))

    ventas = cursor.execute("""SELECT v.id,p.tipo,c.nombre,c.apellido,v.cantidad,v.fecha,v.total
                                 FROM ventas v
                                 JOIN productos p ON v.producto_id=p.id
                                 JOIN clientes c ON v.cliente_id=c.id""").fetchall()

    productos = cursor.execute("SELECT * FROM productos").fetchall()
    clientes = cursor.execute("SELECT * FROM clientes").fetchall()

    db.close()

    return render_template("ventas.html", ventas=ventas, productos=productos, clientes=clientes)

@app.route("/ventas/<int:id>/eliminar", methods=["POST"])
def eliminar_venta(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM ventas WHERE id=?", (id,))
    db.commit()
    db.close()
    return redirect(url_for("ver_ventas"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
