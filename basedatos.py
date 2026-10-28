import sqlite3

DB = "tareas.db"


def crear_tabla():
    with sqlite3.connect(DB) as conexion:
        conexion.execute("""
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                texto TEXT NOT NULL
            )
        """)


def listar():
    with sqlite3.connect(DB) as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT id, texto FROM tareas")
        filas = cursor.fetchall()
    return [{"id": fila[0], "texto": fila[1]} for fila in filas]


def obtener(id):
    with sqlite3.connect(DB) as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT id, texto FROM tareas WHERE id = ?", (id,))
        fila = cursor.fetchone()
    if fila is None:
        return None
    return {"id": fila[0], "texto": fila[1]}


def añadir(texto):
    with sqlite3.connect(DB) as conexion:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO tareas (texto) VALUES (?)", (texto,))
        return cursor.lastrowid


def actualizar(id, texto):
    with sqlite3.connect(DB) as conexion:
        cursor = conexion.cursor()
        cursor.execute("UPDATE tareas SET texto = ? WHERE id = ?", (texto, id))
        return cursor.rowcount > 0


def borrar(id):
    with sqlite3.connect(DB) as conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM tareas WHERE id = ?", (id,))
        return cursor.rowcount > 0


def importar_desde_txt(archivo="tareas.txt"):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            lineas = f.read().splitlines()
    except FileNotFoundError:
        return 0

    for linea in lineas:
        if linea.strip():
            añadir(linea)
    return len(lineas)


crear_tabla()


if __name__ == "__main__":
    nuevo = añadir("estudiar sqlite")
    print(listar())
    print(borrar(nuevo))     # True
    print(borrar(9999))      # False
    print(listar())
