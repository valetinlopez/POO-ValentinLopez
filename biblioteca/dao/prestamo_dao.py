from datetime import date
from dao.database import get_connection
from dao.libro_dao import LibroDAO
from dao.usuario_dao import UsuarioDAO
from domain.prestamo import Prestamo


class PrestamoDAO:
    """
    Responsabilidad única: persistir y recuperar Prestamos desde SQLite.
    Necesita LibroDAO y UsuarioDAO para reconstruir los objetos relacionados.
    """

    def __init__(self):
        # El PrestamoDAO necesita los otros DAOs para reconstruir objetos completos
        self.__libro_dao = LibroDAO()
        self.__usuario_dao = UsuarioDAO()

    def guardar(self, prestamo: Prestamo):
        conn = get_connection()
        try:
            conn.execute(
                """INSERT INTO prestamos
                   (id, usuario_nro_socio, libro_isbn, fecha_inicio,
                    fecha_vencimiento, fecha_devolucion, devuelto)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (
                    prestamo.id,
                    prestamo.usuario.nro_socio,
                    prestamo.libro.isbn,
                    prestamo.fecha_inicio.isoformat(),
                    prestamo.fecha_vencimiento.isoformat(),
                    prestamo.fecha_devolucion.isoformat() if prestamo.fecha_devolucion else None,
                    int(prestamo.devuelto)
                )
            )
            conn.commit()
        finally:
            conn.close()

    def buscar_por_id(self, id_prestamo: int) -> Prestamo | None:
        conn = get_connection()
        try:
            fila = conn.execute(
                "SELECT * FROM prestamos WHERE id = ?", (id_prestamo,)
            ).fetchone()
            return self.__fila_a_prestamo(fila) if fila else None
        finally:
            conn.close()

    def buscar_por_usuario(self, nro_socio: int) -> list[Prestamo]:
        conn = get_connection()
        try:
            filas = conn.execute(
                "SELECT * FROM prestamos WHERE usuario_nro_socio = ? ORDER BY fecha_inicio DESC",
                (nro_socio,)
            ).fetchall()
            return [self.__fila_a_prestamo(f) for f in filas]
        finally:
            conn.close()

    def listar_todos(self) -> list[Prestamo]:
        conn = get_connection()
        try:
            filas = conn.execute(
                "SELECT * FROM prestamos ORDER BY fecha_inicio DESC"
            ).fetchall()
            return [self.__fila_a_prestamo(f) for f in filas]
        finally:
            conn.close()

    def actualizar(self, prestamo: Prestamo):
        """Actualiza el estado del préstamo — principalmente para registrar devoluciones."""
        conn = get_connection()
        try:
            conn.execute(
                """UPDATE prestamos
                   SET devuelto=?, fecha_devolucion=?
                   WHERE id=?""",
                (
                    int(prestamo.devuelto),
                    prestamo.fecha_devolucion.isoformat() if prestamo.fecha_devolucion else None,
                    prestamo.id
                )
            )
            conn.commit()
        finally:
            conn.close()

    def obtener_proximo_id(self) -> int:
        conn = get_connection()
        try:
            fila = conn.execute(
                "SELECT MAX(id) as maximo FROM prestamos"
            ).fetchone()
            maximo = fila["maximo"]
            return (maximo + 1) if maximo is not None else 1
        finally:
            conn.close()

    def __fila_a_prestamo(self, fila) -> Prestamo:
        """
        Reconstruye un objeto Prestamo completo desde SQLite.
        Necesita traer el Usuario y el Libro desde sus DAOs.
        """
        usuario = self.__usuario_dao.buscar_por_nro_socio(fila["usuario_nro_socio"])
        libro   = self.__libro_dao.buscar_por_isbn(fila["libro_isbn"])

        prestamo = Prestamo(fila["id"], usuario, libro)

        # Restauramos el estado de devolución si corresponde
        if fila["devuelto"]:
            prestamo.registrar_devolucion()

        return prestamo