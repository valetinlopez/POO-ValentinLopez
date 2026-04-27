from domain.empleado import Empleado


class Bibliotecario(Empleado):
    """
    Empleado que gestiona préstamos en un sector específico de la biblioteca.
    Puede registrar préstamos, pero con restricciones respecto al Admin.
    """

    def __init__(self, id: int, nombre: str, apellido: str, email: str,
                 legajo: str, salario: float, sector: str):
        super().__init__(id, nombre, apellido, email, legajo, salario)
        self.__sector = sector

    @property
    def sector(self) -> str:
        return self.__sector

    # ---------- Implementación concreta del método abstracto ----------

    def registrar_prestamo(self, prestamo) -> str:
        """
        El bibliotecario puede registrar préstamos solo de su sector.
        Polimorfismo: misma firma que Admin.registrar_prestamo(), distinto comportamiento.
        """
        return (
            f"[Bibliotecario] {self.nombre_completo()} registró el préstamo #{prestamo.id} "
            f"en el sector '{self.__sector}'."
        )

    def descripcion(self) -> str:
        return (
            f"Bibliotecario — {self.nombre_completo()} "
            f"| Sector: {self.__sector} | Legajo: {self.legajo}"
        )