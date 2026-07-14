"""
TP - Métodos heredados de object
Parte 2: Sobrescribimos los métodos especiales para que la clase
se comporte de forma pythonica (comparación por valor, hash
consistente, representación legible, etc.)
"""

from sources.persona_sobreescrita import Persona


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
