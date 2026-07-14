"""Clase Persona con metodos especiales sobrescritos."""

from __future__ import annotations


class Persona:
    """Representa una persona comparada por valor."""

    def __init__(self, nombre: str, edad: int, email: str) -> None:
        self.nombre = nombre
        self.edad = edad
        self.email = email

    def __str__(self) -> str:
        return f"{self.nombre} ({self.edad} años) - {self.email}"

    def __repr__(self) -> str:
        return f"Persona(nombre={self.nombre!r}, edad={self.edad!r}, email={self.email!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Persona):
            return NotImplemented

        return (
            self.nombre == other.nombre
            and self.edad == other.edad
            and self.email == other.email
        )

    def __hash__(self) -> int:
        return hash((self.nombre, self.edad, self.email))

