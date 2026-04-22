# ==========================================
# Constructores de clases - Clase Animal
# ==========================================

class Animal:
    """
    Clase que representa un animal con nombre y especie.
    """

    def __init__(self, nombre, especie):
        """
        Constructor de la clase.
        Se ejecuta automáticamente al crear una instancia.

        Parámetros:
            nombre  (str): El nombre del animal.
            especie (str): La especie del animal.
        """
        self.nombre = nombre
        self.especie = especie

    def setNombre(self, nombre):
        """Modifica el nombre del animal."""
        self.nombre = nombre

    def setEspecie(self, especie):
        """Modifica la especie del animal."""
        self.especie = especie

    def mostrarInfo(self):
        """Muestra la información del animal."""
        print(f"Nombre: {self.nombre} | Especie: {self.especie}")


# ==========================================
# Instancia 1: Firulais
# ==========================================

animal1 = Animal("Firulais", "Perro")
animal1.mostrarInfo()  # Nombre: Firulais | Especie: Perro

# Modificación directa de atributos
animal1.nombre = "Rex"
animal1.especie = "Lobo"
animal1.mostrarInfo()  # Nombre: Rex | Especie: Lobo

# Modificación mediante métodos setter
animal1.setNombre("Max")
animal1.setEspecie("Pastor Alemán")
animal1.mostrarInfo()  # Nombre: Max | Especie: Pastor Alemán


# ==========================================
# Instancia 2: Michi
# ==========================================

animal2 = Animal("Michi", "Gato")
animal2.mostrarInfo()  # Nombre: Michi | Especie: Gato

# Modificación mediante métodos setter
animal2.setNombre("Pelusa")
animal2.setEspecie("Gato Persa")
animal2.mostrarInfo()  # Nombre: Pelusa | Especie: Gato Persa