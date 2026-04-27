from abc import ABC, abstractmethod


class Persona(ABC):
    """
    Clase abstracta que representa a cualquier persona dentro del sistema.
    No se puede instanciar directamente — siempre va a ser un Usuario o un Empleado.
    """

    def __init__(self, id: int, nombre: str, apellido: str, email: str):
        # Encapsulamiento: los atributos son privados (__)
        # Solo se acceden desde afuera a través de los @property
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email

    # ---------- Getters (lectura) ----------

    @property
    def id(self) -> int:
        return self.__id

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def apellido(self) -> str:
        return self.__apellido

    @property
    def email(self) -> str:
        return self.__email

    # ---------- Setters (escritura con validación) ----------

    @nombre.setter
    def nombre(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor.strip()

    @apellido.setter
    def apellido(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("El apellido no puede estar vacío.")
        self.__apellido = valor.strip()

    @email.setter
    def email(self, valor: str):
        if "@" not in valor:
            raise ValueError(f"El email '{valor}' no es válido.")
        self.__email = valor.strip()

    # ---------- Método abstracto (polimorfismo) ----------

    @abstractmethod
    def descripcion(self) -> str:
        """
        Cada subclase DEBE implementar este método.
        Un Bibliotecario se describe distinto a un Usuario.
        """
        pass

    # ---------- Método común a todas las personas ----------

    def nombre_completo(self) -> str:
        return f"{self.__nombre} {self.__apellido}"

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] {self.nombre_completo()} — {self.__email}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.__id}, nombre='{self.__nombre}', apellido='{self.__apellido}')"