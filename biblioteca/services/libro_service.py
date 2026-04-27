from domain.libro import Libro


class LibroService:
    """
    Contiene toda la lógica de negocio relacionada con los libros.
    No sabe nada de base de datos ni de pantallas — solo procesa y decide.
    """

    def __init__(self, libro_dao):
        # Recibe el DAO como dependencia — así el service no depende
        # de UNA implementación concreta de persistencia.
        # Mañana podés cambiar SQLite por MongoDB y este archivo no cambia.
        self.__dao = libro_dao

    # ---------- Operaciones ----------

    def registrar_libro(self, isbn: str, titulo: str, autor: str,
                        genero: str, stock: int) -> Libro:
        """
        Crea un libro nuevo y lo persiste.
        Valida que no exista ya un libro con ese ISBN.
        """
        if not isbn or not titulo or not autor:
            raise ValueError("ISBN, título y autor son obligatorios.")

        if stock < 0:
            raise ValueError("El stock inicial no puede ser negativo.")

        if self.__dao.buscar_por_isbn(isbn):
            raise Exception(f"Ya existe un libro con ISBN '{isbn}'.")

        libro = Libro(isbn, titulo, autor, genero, stock)
        self.__dao.guardar(libro)
        return libro

    def buscar_por_isbn(self, isbn: str) -> Libro:
        """Busca un libro por ISBN. Lanza error si no existe."""
        libro = self.__dao.buscar_por_isbn(isbn)
        if not libro:
            raise Exception(f"No se encontró ningún libro con ISBN '{isbn}'.")
        return libro

    def buscar_por_titulo(self, titulo: str) -> list[Libro]:
        """Devuelve todos los libros cuyo título contenga el texto buscado."""
        if not titulo:
            raise ValueError("El título de búsqueda no puede estar vacío.")
        return self.__dao.buscar_por_titulo(titulo)

    def listar_todos(self) -> list[Libro]:
        """Devuelve el catálogo completo."""
        return self.__dao.listar_todos()

    def listar_disponibles(self) -> list[Libro]:
        """Devuelve solo los libros con stock mayor a 0."""
        return [libro for libro in self.__dao.listar_todos() if libro.disponible]

    def actualizar_stock(self, isbn: str, nuevo_stock: int):
        """Permite al admin corregir el stock manualmente."""
        if nuevo_stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        libro = self.buscar_por_isbn(isbn)
        # Accedemos al DAO para actualizar — el service coordina, no persiste
        self.__dao.actualizar(libro, nuevo_stock)

    def eliminar_libro(self, isbn: str):
        """Elimina un libro del catálogo si no tiene préstamos activos."""
        libro = self.buscar_por_isbn(isbn)
        # Regla de negocio: no se puede eliminar si no está disponible
        # (significa que hay ejemplares prestados)
        if not libro.disponible and libro.stock == 0:
            raise Exception(
                f"No se puede eliminar '{libro.titulo}': tiene ejemplares prestados."
            )
        self.__dao.eliminar(isbn)