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
        print("\n📚 Lista de libros:")
        for libro in self.__libros:
            print(libro.mostrar_info())

    def mostrar_usuarios(self):
        print("\n👤 Lista de usuarios:")
        for usuario in self.__usuarios:
            print(usuario.mostrar_info())