from database.connection import get_connection


def insertar_usuario(nombre):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO usuarios (nombre) VALUES (%s) RETURNING id",
        (nombre,)
    )
    user_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    return user_id


def insertar_libro(titulo, autor, disponible=True):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO libros (titulo, autor, disponible) VALUES (%s, %s, %s) RETURNING id",
        (titulo, autor, disponible)
    )
    libro_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    return libro_id


def registrar_prestamo(usuario_id, libro_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO prestamos (usuario_id, libro_id) VALUES (%s, %s)",
        (usuario_id, libro_id)
    )

    cursor.execute(
        "UPDATE libros SET disponible = FALSE WHERE id = %s",
        (libro_id,)
    )

    conn.commit()
    cursor.close()
    conn.close()