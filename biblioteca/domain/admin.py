from domain.empleado import Empleado


class Admin(Empleado):
    """
    Empleado con acceso total al sistema.
    Puede registrar préstamos de cualquier sector y tiene permisos adicionales.
    """

    def __init__(self, id: int, nombre: str, apellido: str, email: str,
                 legajo: str, salario: float, nivel_acceso: int):
        super().__init__(id, nombre, apellido, email, legajo, salario)

        if nivel_acceso not in (1, 2, 3):
            raise ValueError("El nivel de acceso debe ser 1, 2 o 3.")
        self.__nivel_acceso = nivel_acceso

    @property
    def nivel_acceso(self) -> int:
        return self.__nivel_acceso

    # ---------- Implementación concreta del método abstracto ----------

    def registrar_prestamo(self, prestamo) -> str:
        """
        El Admin puede registrar cualquier préstamo sin restricción de sector.
        Polimorfismo: misma firma que Bibliotecario.registrar_prestamo(), distinto comportamiento.
        """
        return (
            f"[Admin] {self.nombre_completo()} (nivel {self.__nivel_acceso}) "
            f"registró el préstamo #{prestamo.id} con acceso total."
        )

    def descripcion(self) -> str:
        return (
            f"Admin — {self.nombre_completo()} "
            f"| Nivel de acceso: {self.__nivel_acceso} | Legajo: {self.legajo}"
        )