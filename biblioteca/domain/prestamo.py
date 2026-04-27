from datetime import date, timedelta
from domain.libro import Libro
from domain.usuario import Usuario


class Prestamo:
    """
    Representa el acto de que un Usuario toma prestado un Libro.
    Es una entidad propia porque tiene atributos y comportamiento propio:
    fecha de inicio, vencimiento, y estado de devolución.
    """

    DIAS_PRESTAMO = 14  # Regla de negocio: los préstamos duran 14 días

    def __init__(self, id: int, usuario: Usuario, libro: Libro):
        self.__id = id
        self.__usuario = usuario
        self.__libro = libro
        self.__fecha_inicio = date.today()
        self.__fecha_vencimiento = date.today() + timedelta(days=self.DIAS_PRESTAMO)
        self.__fecha_devolucion = None   # None mientras no se devuelva
        self.__devuelto = False

    # ---------- Getters ----------

    @property
    def id(self) -> int:
        return self.__id

    @property
    def usuario(self) -> Usuario:
        return self.__usuario

    @property
    def libro(self) -> Libro:
        return self.__libro

    @property
    def fecha_inicio(self) -> date:
        return self.__fecha_inicio

    @property
    def fecha_vencimiento(self) -> date:
        return self.__fecha_vencimiento

    @property
    def fecha_devolucion(self):
        return self.__fecha_devolucion

    @property
    def devuelto(self) -> bool:
        return self.__devuelto

    # ---------- Métodos ----------

    def esta_vencido(self) -> bool:
        """Devuelve True si el préstamo venció y todavía no se devolvió."""
        return not self.__devuelto and date.today() > self.__fecha_vencimiento

    def registrar_devolucion(self):
        """Marca el préstamo como devuelto y actualiza libro y usuario."""
        if self.__devuelto:
            raise Exception(f"El préstamo #{self.__id} ya fue devuelto.")
        self.__devuelto = True
        self.__fecha_devolucion = date.today()
        self.__libro.devolver()
        self.__usuario.decrementar_prestamos()

    def __str__(self) -> str:
        estado = "devuelto" if self.__devuelto else ("VENCIDO" if self.esta_vencido() else "activo")
        return (
            f"Préstamo #{self.__id} | {self.__usuario.nombre_completo()} → "
            f"'{self.__libro.titulo}' | Vence: {self.__fecha_vencimiento} | Estado: {estado}"
        )