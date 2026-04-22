class Libro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__disponible = True

    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            return True
        return False

    def devolver(self):
        self.__disponible = True

    def mostrar_info(self):
        return f"{self.__titulo} - {self.__autor} | Disponible: {self.__disponible}"

    def esta_disponible(self):
        return self.__disponible


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.__nombre = nombre
        self.__id = id_usuario

    def mostrar_info(self):
        return f"Usuario: {self.__nombre} (ID: {self.__id})"


class Prestamo:
    def __init__(self, usuario, libro):
        self.__usuario = usuario
        self.__libro = libro

    def realizar_prestamo(self):
        if self.__libro.prestar():
            print(f"{self.__usuario.mostrar_info()} tomó prestado '{self.__libro.mostrar_info()}'")
        else:
            print("El libro no está disponible")

    def devolver_libro(self):
        self.__libro.devolver()
        print("Libro devuelto")


class Biblioteca:
    def __init__(self):
        self.__libros = []
        self.__usuarios = []
        self.__prestamos = []

    def agregar_libro(self, libro):
        self.__libros.append(libro)

    def agregar_usuario(self, usuario):
        self.__usuarios.append(usuario)

    def registrar_prestamo(self, prestamo):
        self.__prestamos.append(prestamo)

    def mostrar_libros(self):
        for libro in self.__libros:
            print(libro.mostrar_info())
            
            
# PROGRAMA PRINCIPAL
# Crear biblioteca
biblio = Biblioteca()

# Crear objetos
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry")
usuario1 = Usuario("Juan", 1)

# Agregar a biblioteca
biblio.agregar_libro(libro1)
biblio.agregar_usuario(usuario1)

# Crear préstamo
prestamo1 = Prestamo(usuario1, libro1)

# Ejecutar acciones
prestamo1.realizar_prestamo()
biblio.mostrar_libros()  
