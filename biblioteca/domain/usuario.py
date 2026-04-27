from datetime import date
from domain.persona import Persona


class Usuario(Persona):
    """
    Representa a una persona que puede sacar libros en préstamo.
    Hereda nombre, apellido, email de Persona.
    Agrega lo específico de un socio de la biblioteca.
    """

    MAX_PRESTAMOS = 3  # Regla de negocio: un usuario no puede tener más de 3 préstamos activos

    def __init__(self, id: int, nombre: str, apellido: str, email: str, nro_socio: int):
        # Llamamos al __init__ del padre para no repetir código
        super().__init__(id, nombre, apellido, email)

        self.__nro_socio = nro_socio
        self.__fecha_alta = date.today()
        self.__activo = True
        self.__prestamos_activos = 0

    # ---------- Getters ----------

    @property
    def nro_socio(self) -> int:
        return self.__nro_socio

    @property
    def fecha_alta(self) -> date:
        return self.__fecha_alta

    @property
    def activo(self) -> bool:
        return self.__activo

    @property
    def prestamos_activos(self) -> int:
        return self.__prestamos_activos

    # ---------- Setters ----------

    @activo.setter
    def activo(self, valor: bool):
        self.__activo = valor

    # ---------- Métodos propios de Usuario ----------

    def puede_pedir_prestamo(self) -> bool:
        """Verifica si el usuario está activo y no superó el límite de préstamos."""
        return self.__activo and self.__prestamos_activos < self.MAX_PRESTAMOS

    def incrementar_prestamos(self):
        """Se llama cuando se le asigna un nuevo préstamo."""
        if not self.puede_pedir_prestamo():
            raise Exception(f"{self.nombre_completo()} no puede tomar más préstamos.")
        self.__prestamos_activos += 1

    def decrementar_prestamos(self):
        """Se llama cuando devuelve un libro."""
        if self.__prestamos_activos > 0:
            self.__prestamos_activos -= 1

    def dar_de_baja(self):
        """Desactiva el usuario en el sistema."""
        self.__activo = False
        print(f"Usuario {self.nombre_completo()} dado de baja.")

    # ---------- Implementación del método abstracto ----------

    def descripcion(self) -> str:
        estado = "activo" if self.__activo else "inactivo"
        return (
            f"Usuario #{self.__nro_socio} — {self.nombre_completo()} "
            f"| Préstamos activos: {self.__prestamos_activos}/{self.MAX_PRESTAMOS} "
            f"| Estado: {estado}"
        )