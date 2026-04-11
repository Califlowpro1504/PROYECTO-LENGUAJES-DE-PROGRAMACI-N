import sqlite3

def crear_db():
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        precio REAL,
        cantidad INTEGER
    )
    """)

    conn.commit()
    conn.close()

crear_db()
