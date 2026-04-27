class Libro:
    """
    Representa un libro físico del catálogo de la biblioteca.
    No hereda de Persona — es una entidad independiente del dominio.
    """

    def __init__(self, isbn: str, titulo: str, autor: str, genero: str, stock: int):
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__stock = stock

    # ---------- Getters ----------

    @property
    def isbn(self) -> str:
        return self.__isbn

    @property
    def titulo(self) -> str:
        return self.__titulo

    @property
    def autor(self) -> str:
        return self.__autor

    @property
    def genero(self) -> str:
        return self.__genero

    @property
    def stock(self) -> int:
        return self.__stock

    @property
    def disponible(self) -> bool:
        """Un libro está disponible si tiene al menos 1 ejemplar en stock."""
        return self.__stock > 0

    # ---------- Métodos ----------

    def prestar(self):
        """Descuenta un ejemplar del stock cuando se presta."""
        if not self.disponible:
            raise Exception(f"No hay ejemplares disponibles de '{self.__titulo}'.")
        self.__stock -= 1

    def devolver(self):
        """Suma un ejemplar al stock cuando se devuelve."""
        self.__stock += 1

    def __str__(self) -> str:
        estado = "disponible" if self.disponible else "sin stock"
        return f"'{self.__titulo}' — {self.__autor} | ISBN: {self.__isbn} | Stock: {self.__stock} ({estado})"

    def __repr__(self) -> str:
        return f"Libro(isbn='{self.__isbn}', titulo='{self.__titulo}', stock={self.__stock})"