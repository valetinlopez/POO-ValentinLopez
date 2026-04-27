from domain.usuario import Usuario


class UsuarioService:
    """
    Contiene toda la lógica de negocio relacionada con los usuarios/socios.
    """

    def __init__(self, usuario_dao):
        self.__dao = usuario_dao
        self.__proximo_nro_socio = self.__dao.obtener_proximo_nro_socio()

    # ---------- Operaciones ----------

    def registrar_usuario(self, id: int, nombre: str, apellido: str,
                          email: str) -> Usuario:
        """
        Da de alta un nuevo socio.
        El nro_socio se asigna automáticamente — el usuario no lo elige.
        """
        if not nombre or not apellido or not email:
            raise ValueError("Nombre, apellido y email son obligatorios.")

        if self.__dao.buscar_por_email(email):
            raise Exception(f"Ya existe un usuario con el email '{email}'.")

        nro_socio = self.__proximo_nro_socio
        usuario = Usuario(id, nombre, apellido, email, nro_socio)
        self.__dao.guardar(usuario)
        self.__proximo_nro_socio += 1
        return usuario

    def buscar_por_nro_socio(self, nro_socio: int) -> Usuario:
        usuario = self.__dao.buscar_por_nro_socio(nro_socio)
        if not usuario:
            raise Exception(f"No se encontró el socio #{nro_socio}.")
        return usuario

    def buscar_por_email(self, email: str) -> Usuario:
        usuario = self.__dao.buscar_por_email(email)
        if not usuario:
            raise Exception(f"No se encontró ningún usuario con email '{email}'.")
        return usuario

    def listar_todos(self) -> list[Usuario]:
        return self.__dao.listar_todos()

    def listar_activos(self) -> list[Usuario]:
        return [u for u in self.__dao.listar_todos() if u.activo]

    def dar_de_baja(self, nro_socio: int):
        """
        Desactiva un socio.
        Regla de negocio: no se puede dar de baja si tiene préstamos activos.
        """
        usuario = self.buscar_por_nro_socio(nro_socio)

        if usuario.prestamos_activos > 0:
            raise Exception(
                f"{usuario.nombre_completo()} tiene {usuario.prestamos_activos} "
                f"préstamo(s) activo(s). Debe devolver los libros antes de darse de baja."
            )

        usuario.dar_de_baja()
        self.__dao.actualizar(usuario)