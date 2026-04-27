"""
DAOs en memoria (sin base de datos).
Simulan la persistencia usando listas y diccionarios de Python.
Esto nos permite probar la lógica de los services sin depender de SQLite todavía.
Después, cuando implementemos el DAO real, los services no van a cambiar en absoluto.
"""


class LibroDaoMemoria:
    def __init__(self):
        self.__libros = {}  # isbn → Libro

    def guardar(self, libro):
        self.__libros[libro.isbn] = libro

    def buscar_por_isbn(self, isbn):
        return self.__libros.get(isbn)

    def buscar_por_titulo(self, titulo):
        titulo_lower = titulo.lower()
        return [l for l in self.__libros.values() if titulo_lower in l.titulo.lower()]

    def listar_todos(self):
        return list(self.__libros.values())

    def actualizar(self, libro, nuevo_stock=None):
        self.__libros[libro.isbn] = libro

    def eliminar(self, isbn):
        self.__libros.pop(isbn, None)


class UsuarioDaoMemoria:
    def __init__(self):
        self.__usuarios = {}   # nro_socio → Usuario
        self.__por_email = {}  # email → Usuario

    def guardar(self, usuario):
        self.__usuarios[usuario.nro_socio] = usuario
        self.__por_email[usuario.email] = usuario

    def buscar_por_nro_socio(self, nro_socio):
        return self.__usuarios.get(nro_socio)

    def buscar_por_email(self, email):
        return self.__por_email.get(email)

    def listar_todos(self):
        return list(self.__usuarios.values())

    def actualizar(self, usuario):
        self.__usuarios[usuario.nro_socio] = usuario

    def obtener_proximo_nro_socio(self):
        return max(self.__usuarios.keys(), default=0) + 1


class PrestamoDaoMemoria:
    def __init__(self):
        self.__prestamos = {}  # id → Prestamo

    def guardar(self, prestamo):
        self.__prestamos[prestamo.id] = prestamo

    def buscar_por_id(self, id_prestamo):
        return self.__prestamos.get(id_prestamo)

    def buscar_por_usuario(self, nro_socio):
        return [p for p in self.__prestamos.values()
                if p.usuario.nro_socio == nro_socio]

    def listar_todos(self):
        return list(self.__prestamos.values())

    def actualizar(self, prestamo):
        self.__prestamos[prestamo.id] = prestamo

    def obtener_proximo_id(self):
        return max(self.__prestamos.keys(), default=0) + 1