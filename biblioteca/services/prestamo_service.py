from domain.prestamo import Prestamo
from domain.empleado import Empleado


class PrestamoService:
    """
    Contiene la lógica de negocio del proceso de préstamo y devolución.
    Es la más crítica del sistema — coordina Usuario, Libro y Empleado.
    """

    def __init__(self, prestamo_dao, libro_dao, usuario_dao):
        self.__dao = prestamo_dao
        self.__libro_dao = libro_dao
        self.__usuario_dao = usuario_dao
        self.__proximo_id = self.__dao.obtener_proximo_id()

    # ---------- Operaciones principales ----------

    def realizar_prestamo(self, nro_socio: int, isbn: str,
                          empleado: Empleado) -> Prestamo:
        """
        Proceso completo de préstamo.
        Valida todas las condiciones antes de confirmar.

        Reglas de negocio aplicadas:
          1. El usuario debe existir y estar activo.
          2. El usuario no puede superar el límite de préstamos (MAX_PRESTAMOS).
          3. El libro debe existir y tener stock disponible.
          4. Si todo está bien, se crea el préstamo y se actualizan libro y usuario.
        """
        # Regla 1 y 2: validar usuario
        usuario = self.__usuario_dao.buscar_por_nro_socio(nro_socio)
        if not usuario:
            raise Exception(f"No se encontró el socio #{nro_socio}.")

        if not usuario.puede_pedir_prestamo():
            if not usuario.activo:
                raise Exception(f"{usuario.nombre_completo()} está dado de baja.")
            raise Exception(
                f"{usuario.nombre_completo()} alcanzó el límite de "
                f"{usuario.MAX_PRESTAMOS} préstamos activos."
            )

        # Regla 3: validar libro
        libro = self.__libro_dao.buscar_por_isbn(isbn)
        if not libro:
            raise Exception(f"No se encontró el libro con ISBN '{isbn}'.")

        if not libro.disponible:
            raise Exception(f"'{libro.titulo}' no tiene ejemplares disponibles.")

        # Regla 4: todo OK — ejecutar el préstamo
        libro.prestar()
        usuario.incrementar_prestamos()

        prestamo = Prestamo(self.__proximo_id, usuario, libro)
        self.__proximo_id += 1

        # Persistir los cambios
        self.__dao.guardar(prestamo)
        self.__libro_dao.actualizar(libro, libro.stock)
        self.__usuario_dao.actualizar(usuario)

        # Polimorfismo: el empleado registra según su tipo (Bibliotecario o Admin)
        mensaje = empleado.registrar_prestamo(prestamo)
        print(f"  ✓ {mensaje}")

        return prestamo

    def registrar_devolucion(self, id_prestamo: int) -> Prestamo:
        """
        Procesa la devolución de un libro.

        Reglas de negocio:
          1. El préstamo debe existir.
          2. No puede estar ya devuelto.
          3. Se actualiza libro y usuario automáticamente.
        """
        prestamo = self.__dao.buscar_por_id(id_prestamo)
        if not prestamo:
            raise Exception(f"No se encontró el préstamo #{id_prestamo}.")

        # El método de Prestamo valida si ya fue devuelto
        prestamo.registrar_devolucion()

        # Persistir los cambios
        self.__dao.actualizar(prestamo)
        self.__libro_dao.actualizar(prestamo.libro, prestamo.libro.stock)
        self.__usuario_dao.actualizar(prestamo.usuario)

        return prestamo

    # ---------- Consultas ----------

    def listar_activos(self) -> list[Prestamo]:
        """Devuelve todos los préstamos que no fueron devueltos."""
        return [p for p in self.__dao.listar_todos() if not p.devuelto]

    def listar_vencidos(self) -> list[Prestamo]:
        """Devuelve todos los préstamos vencidos sin devolver — útil para alertas."""
        return [p for p in self.__dao.listar_todos() if p.esta_vencido()]

    def historial_usuario(self, nro_socio: int) -> list[Prestamo]:
        """Devuelve todos los préstamos (activos e históricos) de un socio."""
        usuario = self.__usuario_dao.buscar_por_nro_socio(nro_socio)
        if not usuario:
            raise Exception(f"No se encontró el socio #{nro_socio}.")
        return self.__dao.buscar_por_usuario(nro_socio)