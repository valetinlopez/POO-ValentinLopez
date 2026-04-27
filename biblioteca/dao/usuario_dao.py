from datetime import date
from dao.database import get_connection
from domain.usuario import Usuario


class UsuarioDAO:
    """
    Responsabilidad única: persistir y recuperar Usuarios desde SQLite.
    """

    def guardar(self, usuario: Usuario):
        conn = get_connection()
        try:
            conn.execute(
                """INSERT INTO usuarios
                   (id, nombre, apellido, email, nro_socio, fecha_alta, activo, prestamos_activos)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    usuario.id,
                    usuario.nombre,
                    usuario.apellido,
                    usuario.email,
                    usuario.nro_socio,
                    usuario.fecha_alta.isoformat(),
                    int(usuario.activo),
                    usuario.prestamos_activos
                )
            )
            conn.commit()
        finally:
            conn.close()

    def buscar_por_nro_socio(self, nro_socio: int) -> Usuario | None:
        conn = get_connection()
        try:
            fila = conn.execute(
                "SELECT * FROM usuarios WHERE nro_socio = ?", (nro_socio,)
            ).fetchone()
            return self.__fila_a_usuario(fila) if fila else None
        finally:
            conn.close()

    def buscar_por_email(self, email: str) -> Usuario | None:
        conn = get_connection()
        try:
            fila = conn.execute(
                "SELECT * FROM usuarios WHERE email = ?", (email,)
            ).fetchone()
            return self.__fila_a_usuario(fila) if fila else None
        finally:
            conn.close()

    def listar_todos(self) -> list[Usuario]:
        conn = get_connection()
        try:
            filas = conn.execute(
                "SELECT * FROM usuarios ORDER BY apellido, nombre"
            ).fetchall()
            return [self.__fila_a_usuario(f) for f in filas]
        finally:
            conn.close()

    def actualizar(self, usuario: Usuario):
        """Sincroniza el estado del objeto Usuario con la base de datos."""
        conn = get_connection()
        try:
            conn.execute(
                """UPDATE usuarios
                   SET nombre=?, apellido=?, email=?, activo=?, prestamos_activos=?
                   WHERE nro_socio=?""",
                (
                    usuario.nombre,
                    usuario.apellido,
                    usuario.email,
                    int(usuario.activo),
                    usuario.prestamos_activos,
                    usuario.nro_socio
                )
            )
            conn.commit()
        finally:
            conn.close()

    def obtener_proximo_nro_socio(self) -> int:
        """Calcula el próximo número de socio disponible."""
        conn = get_connection()
        try:
            fila = conn.execute(
                "SELECT MAX(nro_socio) as maximo FROM usuarios"
            ).fetchone()
            maximo = fila["maximo"]
            return (maximo + 1) if maximo is not None else 1
        finally:
            conn.close()

    def __fila_a_usuario(self, fila) -> Usuario:
        """
        Reconstruye un objeto Usuario desde una fila de SQLite.
        Nótese que reconstruimos el estado interno (activo, prestamos_activos)
        que normalmente solo el objeto maneja — el DAO necesita este acceso especial.
        """
        usuario = Usuario(
            id=fila["id"],
            nombre=fila["nombre"],
            apellido=fila["apellido"],
            email=fila["email"],
            nro_socio=fila["nro_socio"]
        )
        # Restauramos el estado guardado en la base de datos
        if not fila["activo"]:
            usuario.dar_de_baja()

        # Reconstruimos los préstamos activos usando el setter interno
        for _ in range(fila["prestamos_activos"]):
            usuario.incrementar_prestamos()

        return usuario