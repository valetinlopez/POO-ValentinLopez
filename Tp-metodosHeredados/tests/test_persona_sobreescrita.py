import unittest

from sources.persona_sobreescrita import Persona


class TestPersonaSobreescrita(unittest.TestCase):
    def setUp(self) -> None:
        self.persona1 = Persona("Ana", 30, "ana@mail.com")
        self.persona2 = Persona("Ana", 30, "ana@mail.com")
        self.persona3 = Persona("Luis", 25, "luis@mail.com")

    def test_str_devuelve_texto_legible(self) -> None:
        self.assertEqual(str(self.persona1), "Ana (30 años) - ana@mail.com")

    def test_repr_devuelve_texto_preciso(self) -> None:
        self.assertEqual(
            repr(self.persona1),
            "Persona(nombre='Ana', edad=30, email='ana@mail.com')",
        )

    def test_eq_compara_por_valor(self) -> None:
        self.assertEqual(self.persona1, self.persona2)
        self.assertNotEqual(self.persona1, self.persona3)

    def test_hash_es_consistente_con_eq(self) -> None:
        self.assertEqual(hash(self.persona1), hash(self.persona2))
        self.assertEqual(len({self.persona1, self.persona2}), 1)

    def test_type_y_dir(self) -> None:
        self.assertIs(type(self.persona1), Persona)
        self.assertIn("__str__", dir(self.persona1))
        self.assertIn("__repr__", dir(self.persona1))
        self.assertIn("__eq__", dir(self.persona1))
        self.assertIn("__hash__", dir(self.persona1))


if __name__ == "__main__":
    unittest.main()
