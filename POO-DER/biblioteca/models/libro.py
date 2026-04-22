class Libro:
    def __init__(self, titulo, autor, id_libro=None):
        self.__id = id_libro
        self.__titulo = titulo
        self.__autor = autor
        self.__disponible = True

    def set_id(self, id_libro):
        self.__id = id_libro

    def get_id(self):
        return self.__id

    def mostrar_info(self):
        return f"[{self.__id}] {self.__titulo} - {self.__autor}"