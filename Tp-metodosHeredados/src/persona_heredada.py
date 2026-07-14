"""Clase Persona usando los metodos heredados de object."""


class Persona:
    """Representa una persona sin sobrescribir metodos especiales."""

    def __init__(self, nombre: str, edad: int, email: str) -> None:
        self.nombre = nombre
        self.edad = edad
        self.email = email

