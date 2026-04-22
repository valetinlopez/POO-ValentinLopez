class Prestamo:
    def __init__(self, usuario, libro):
        self.__usuario = usuario
        self.__libro = libro

    def realizar_prestamo(self):
        if self.__libro.prestar():
            print(f"{self.__usuario.mostrar_info()} tomó prestado '{self.__libro.mostrar_info()}'")
            return True
        else:
            print("El libro no está disponible")
            return False

    def devolver_libro(self):
        self.__libro.devolver()
        print("Libro devuelto")