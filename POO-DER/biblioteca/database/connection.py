import os
import psycopg2
from psycopg2 import OperationalError


def get_connection():
    try:
        return psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            database=os.getenv("DB_NAME", "biblioteca"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", "tu_password")
        )
    except UnicodeDecodeError as exc:
        decoded = None
        if isinstance(exc.object, (bytes, bytearray)):
            try:
                decoded = exc.object.decode("cp1252")
            except Exception:
                decoded = repr(exc.object)
        raise OperationalError(
            "Error al conectar a PostgreSQL. Verifica usuario, contraseña y que el servidor esté en funcionamiento. "
            f"Mensaje original: {decoded or exc}"
        ) from exc
    except OperationalError as exc:
        raise OperationalError(
            "Error al conectar a PostgreSQL. Verifica usuario, contraseña, base de datos y que PostgreSQL esté ejecutándose."
        ) from exc