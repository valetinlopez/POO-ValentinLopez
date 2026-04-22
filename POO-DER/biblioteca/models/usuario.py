class Usuario:
    def __init__(self, nombre, id_usuario=None):
        self.__id = id_usuario
        self.__nombre = nombre

    def set_id(self, id_usuario):
        self.__id = id_usuario

    def get_id(self):
        return self.__id

    def mostrar_info(self):
        return f"[{self.__id}] {self.__nombre}"