from services.libro_service import LibroService
from services.usuario_service import UsuarioService
from services.prestamo_service import PrestamoService
from domain.empleado import Empleado


class BibliotecaController:
    """
    Intermediario entre la Vista y los Services.
    Recibe pedidos de la vista, delega al service, devuelve resultados.

    La vista nunca habla directamente con los services.
    El controlador nunca muestra nada por pantalla — solo retorna datos o lanza errores.
    """

    def __init__(self, libro_service: LibroService,
                 usuario_service: UsuarioService,
                 prestamo_service: PrestamoService,
                 empleado_activo: Empleado):

        self.__libro_svc   = libro_service
        self.__usuario_svc = usuario_service
        self.__prestamo_svc = prestamo_service
        # El empleado que está usando el sistema en esta sesión
        self.__empleado_activo = empleado_activo

    # ================================================================
    # Libros
    # ================================================================

    def registrar_libro(self, isbn, titulo, autor, genero, stock):
        """Delega al service y devuelve el libro creado."""
        return self.__libro_svc.registrar_libro(isbn, titulo, autor, genero, stock)

    def buscar_libro_por_isbn(self, isbn):
        return self.__libro_svc.buscar_por_isbn(isbn)

    def buscar_libros_por_titulo(self, titulo):
        return self.__libro_svc.buscar_por_titulo(titulo)

    def listar_libros(self):
        return self.__libro_svc.listar_todos()

    def listar_libros_disponibles(self):
        return self.__libro_svc.listar_disponibles()

    def eliminar_libro(self, isbn):
        self.__libro_svc.eliminar_libro(isbn)

    # ================================================================
    # Usuarios
    # ================================================================

    def registrar_usuario(self, id, nombre, apellido, email):
        return self.__usuario_svc.registrar_usuario(id, nombre, apellido, email)

    def buscar_usuario(self, nro_socio):
        return self.__usuario_svc.buscar_por_nro_socio(nro_socio)

    def listar_usuarios(self):
        return self.__usuario_svc.listar_todos()

    def dar_de_baja_usuario(self, nro_socio):
        self.__usuario_svc.dar_de_baja(nro_socio)

    # ================================================================
    # Préstamos
    # ================================================================

    def realizar_prestamo(self, nro_socio, isbn):
        """
        El controlador inyecta el empleado activo de la sesión.
        La vista no necesita saber quién es el empleado — eso es trabajo del controlador.
        """
        return self.__prestamo_svc.realizar_prestamo(
            nro_socio, isbn, self.__empleado_activo
        )

    def registrar_devolucion(self, id_prestamo):
        return self.__prestamo_svc.registrar_devolucion(id_prestamo)

    def listar_prestamos_activos(self):
        return self.__prestamo_svc.listar_activos()

    def listar_prestamos_vencidos(self):
        return self.__prestamo_svc.listar_vencidos()

    def historial_usuario(self, nro_socio):
        return self.__prestamo_svc.historial_usuario(nro_socio)

    # ================================================================
    # Sesión
    # ================================================================

    def obtener_empleado_activo(self):
        return self.__empleado_activo