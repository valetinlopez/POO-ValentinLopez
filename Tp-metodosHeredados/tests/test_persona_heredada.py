import unittest

from sources.persona_heredada import Persona


class TestPersonaHeredada(unittest.TestCase):
    def setUp(self) -> None:
        self.persona1 = Persona("Ana", 30, "ana@mail.com")
        self.persona2 = Persona("Ana", 30, "ana@mail.com")

    def test_guarda_los_atributos(self) -> None:
        self.assertEqual(self.persona1.nombre, "Ana")
        self.assertEqual(self.persona1.edad, 30)
        self.assertEqual(self.persona1.email, "ana@mail.com")

    def test_str_y_repr_usan_representacion_por_defecto(self) -> None:
        self.assertEqual(str(self.persona1), repr(self.persona1))
        self.assertIn("Persona object at", repr(self.persona1))

    def test_eq_compara_identidad_por_defecto(self) -> None:
        self.assertNotEqual(self.persona1, self.persona2)
        self.assertEqual(self.persona1, self.persona1)

    def test_hash_es_el_heredado_de_object(self) -> None:
        self.assertIsInstance(hash(self.persona1), int)
        self.assertEqual(hash(self.persona1), object.__hash__(self.persona1))

    def test_type_y_dir(self) -> None:
        self.assertIs(type(self.persona1), Persona)
        self.assertIn("__str__", dir(self.persona1))
        self.assertIn("__repr__", dir(self.persona1))
        self.assertIn("__eq__", dir(self.persona1))
        self.assertIn("__hash__", dir(self.persona1))
        self.assertIn("nombre", dir(self.persona1))
        self.assertIn("edad", dir(self.persona1))
        self.assertIn("email", dir(self.persona1))


if __name__ == "__main__":
    unittest.main()

