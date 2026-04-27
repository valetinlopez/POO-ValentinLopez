import sqlite3
import os

# Ruta de la base de datos — un solo archivo para todo el sistema
DB_PATH = os.path.join(os.path.dirname(__file__), "biblioteca.db")


def get_connection() -> sqlite3.Connection:
    """
    Devuelve una conexión a la base de datos SQLite.
    row_factory = Row permite acceder a las columnas por nombre (fila["titulo"])
    en vez de por índice (fila[1]) — mucho más legible.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")  # Activar claves foráneas
    return conn


def inicializar_db():
    """
    Crea todas las tablas si no existen.
    Se llama UNA sola vez al arrancar el sistema.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS libros (
            isbn        TEXT PRIMARY KEY,
            titulo      TEXT NOT NULL,
            autor       TEXT NOT NULL,
            genero      TEXT NOT NULL,
            stock       INTEGER NOT NULL CHECK (stock >= 0)
        );

        CREATE TABLE IF NOT EXISTS usuarios (
            id              INTEGER PRIMARY KEY,
            nombre          TEXT NOT NULL,
            apellido        TEXT NOT NULL,
            email           TEXT NOT NULL UNIQUE,
            nro_socio       INTEGER NOT NULL UNIQUE,
            fecha_alta      TEXT NOT NULL,
            activo          INTEGER NOT NULL DEFAULT 1,
            prestamos_activos INTEGER NOT NULL DEFAULT 0
        );

        CREATE TABLE IF NOT EXISTS prestamos (
            id                  INTEGER PRIMARY KEY,
            usuario_nro_socio   INTEGER NOT NULL,
            libro_isbn          TEXT NOT NULL,
            fecha_inicio        TEXT NOT NULL,
            fecha_vencimiento   TEXT NOT NULL,
            fecha_devolucion    TEXT,
            devuelto            INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY (usuario_nro_socio) REFERENCES usuarios(nro_socio),
            FOREIGN KEY (libro_isbn)        REFERENCES libros(isbn)
        );
    """)

    conn.commit()
    conn.close()
    print("Base de datos inicializada correctamente.")