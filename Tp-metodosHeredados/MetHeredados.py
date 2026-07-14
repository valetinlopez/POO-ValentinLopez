"""
TP - Métodos heredados de object

En este archivo se usa una clase Persona sin sobrescribir métodos
especiales. Así se puede observar el comportamiento heredado de object:
__str__, __repr__, __eq__, __hash__, type() y dir().
"""

from sources.persona_heredada import Persona


def main() -> None:
    persona1 = Persona("Ana", 30, "ana@mail.com")
    persona2 = Persona("Ana", 30, "ana@mail.com")

    print("=" * 60)
    print("1) Imprimir el objeto directamente")
    print(persona1)

    print("=" * 60)
    print("2) Usar str(persona1)")
    print(str(persona1))

    print("=" * 60)
    print("3) Usar repr(persona1)")
    print(repr(persona1))

    print("=" * 60)
    print("4) Comparar dos objetos con los mismos datos")
    print("persona1 == persona2:", persona1 == persona2)

    print("=" * 60)
    print("5) Obtener el hash de cada objeto")
    print("hash(persona1):", hash(persona1))
    print("hash(persona2):", hash(persona2))

    print("=" * 60)
    print("6) Mostrar el tipo con type()")
    print(type(persona1))

    print("=" * 60)
    print("7) Mostrar atributos y métodos con dir()")
    print(dir(persona1))


if __name__ == "__main__":
    main()
