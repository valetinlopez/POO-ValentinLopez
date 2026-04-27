from abc import abstractmethod
from domain.persona import Persona


class Empleado(Persona):
    """
    Clase abstracta intermedia. Representa a cualquier empleado de la biblioteca.
    Hereda de Persona y agrega datos laborales.
    No se instancia directamente — siempre será Bibliotecario o Admin.
    """

    def __init__(self, id: int, nombre: str, apellido: str, email: str,
                 legajo: str, salario: float):
        super().__init__(id, nombre, apellido, email)

        self.__legajo = legajo
        self.__salario = salario

    # ---------- Getters ----------

    @property
    def legajo(self) -> str:
        return self.__legajo

    @property
    def salario(self) -> float:
        return self.__salario

    # ---------- Setters ----------

    @salario.setter
    def salario(self, valor: float):
        if valor < 0:
            raise ValueError("El salario no puede ser negativo.")
        self.__salario = valor

    # ---------- Método abstracto (polimorfismo) ----------

    @abstractmethod
    def registrar_prestamo(self, prestamo) -> str:
        """
        Cada tipo de empleado registra un préstamo de forma distinta.
        Aquí es donde se aplica el polimorfismo: misma firma, distinto comportamiento.
        """
        pass

    # ---------- Implementación del método de Persona ----------

    def descripcion(self) -> str:
        return (
            f"Empleado | Legajo: {self.__legajo} — {self.nombre_completo()} "
            f"| Cargo: {self.__class__.__name__} | Salario: ${self.__salario:,.2f}"
        )