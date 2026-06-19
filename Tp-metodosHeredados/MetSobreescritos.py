"""
TP - Métodos heredados de object
Parte 2: Sobrescribimos los métodos especiales para que la clase
se comporte de forma "Pythónica" (comparación por valor, hash
consistente, representación legible, etc.)
"""

from __future__ import annotations


class Persona:
    """Representa una persona con nombre, edad y email.

    Buenas prácticas aplicadas:
    - Type hints en atributos y métodos.
    - __repr__ : representación NO ambigua, pensada para developers/debug.
      Convención: debería poder "reconstruir" el objeto (eval(repr(obj))).
    - __str__  : representación legible, pensada para el usuario final.
      Si no se define, Python usa __repr__ como fallback.
    - __eq__   : compara por VALOR (mismos datos), no por identidad.
      Se valida el tipo con isinstance antes de comparar.
    - __hash__ : se redefine en conjunto con __eq__, usando los MISMOS
      atributos, para respetar el contrato hash <-> igualdad de Python:
      "si a == b, entonces hash(a) == hash(b)".
    """

    def __init__(self, nombre: str, edad: int, email: str) -> None:
        self.nombre = nombre
        self.edad = edad
        self.email = email

    def __str__(self) -> str:
        # Pensado para el usuario final (print, str())
        return f"{self.nombre} ({self.edad} años) - {self.email}"

    def __repr__(self) -> str:
        # Pensado para debugging / logs, sin ambigüedad
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
        # Debe basarse en los mismos campos que __eq__
        return hash((self.nombre, self.edad, self.email))


def main() -> None:
    p1 = Persona("Ana", 30, "ana@mail.com")
    p2 = Persona("Ana", 30, "ana@mail.com")

    print("=" * 60)
    print("1) Imprimir el objeto directamente -> print(p1)")
    print(p1)

    print("=" * 60)
    print("2) str(p1)")
    print(str(p1))

    print("=" * 60)
    print("3) repr(p1)")
    print(repr(p1))

    print("=" * 60)
    print("4) Comparación p1 == p2 (ahora por VALOR)")
    print(p1 == p2)

    print("=" * 60)
    print("5) hash(p1) y hash(p2) (ahora son IGUALES)")
    print(hash(p1))
    print(hash(p2))
    print("¿hash(p1) == hash(p2)? ->", hash(p1) == hash(p2))

    print("=" * 60)
    print("6) type(p1)")
    print(type(p1))

    print("=" * 60)
    print("7) dir(p1)")
    print(dir(p1))

    print("=" * 60)
    print("8) Bonus: usar Persona como clave de dict / elemento de set")
    personas_unicas = {p1, p2}
    print("Cantidad de elementos en el set:", len(personas_unicas))
    # da 1, porque p1 y p2 son "iguales" en valor y hash


if __name__ == "__main__":
    main()