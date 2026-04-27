from dao.database import get_connection
from domain.libro import Libro


class LibroDAO:
    """
    Responsabilidad única: persistir y recuperar Libros desde SQLite.
    No valida reglas de negocio — eso es trabajo del LibroService.
    """

    def guardar(self, libro: Libro):
        """Inserta un libro nuevo en la tabla libros."""
        conn = get_connection()
        try:
            conn.execute(
                "INSERT INTO libros (isbn, titulo, autor, genero, stock) VALUES (?, ?, ?, ?, ?)",
                (libro.isbn, libro.titulo, libro.autor, libro.genero, libro.stock)
            )
            conn.commit()
        finally:
            conn.close()

    def buscar_por_isbn(self, isbn: str) -> Libro | None:
        """Busca un libro por ISBN. Devuelve None si no existe."""
        conn = get_connection()
        try:
            fila = conn.execute(
                "SELECT * FROM libros WHERE isbn = ?", (isbn,)
            ).fetchone()
            return self.__fila_a_libro(fila) if fila else None
        finally:
            conn.close()

    def buscar_por_titulo(self, titulo: str) -> list[Libro]:
        """Búsqueda parcial por título (case-insensitive)."""
        conn = get_connection()
        try:
            filas = conn.execute(
                "SELECT * FROM libros WHERE titulo LIKE ?", (f"%{titulo}%",)
            ).fetchall()
            return [self.__fila_a_libro(f) for f in filas]
        finally:
            conn.close()

    def listar_todos(self) -> list[Libro]:
        """Devuelve todos los libros del catálogo."""
        conn = get_connection()
        try:
            filas = conn.execute("SELECT * FROM libros ORDER BY titulo").fetchall()
            return [self.__fila_a_libro(f) for f in filas]
        finally:
            conn.close()

    def actualizar(self, libro: Libro, nuevo_stock: int = None):
        """Actualiza el stock de un libro. Si no se pasa nuevo_stock, usa el del objeto."""
        stock = nuevo_stock if nuevo_stock is not None else libro.stock
        conn = get_connection()
        try:
            conn.execute(
                "UPDATE libros SET stock = ? WHERE isbn = ?",
                (stock, libro.isbn)
            )
            conn.commit()
        finally:
            conn.close()

    def eliminar(self, isbn: str):
        """Elimina un libro por ISBN."""
        conn = get_connection()
        try:
            conn.execute("DELETE FROM libros WHERE isbn = ?", (isbn,))
            conn.commit()
        finally:
            conn.close()

    def __fila_a_libro(self, fila) -> Libro:
        """
        Convierte una fila de SQLite en un objeto Libro.
        Este método es privado — solo lo usa el DAO internamente.
        Es el puente entre el mundo relacional y el mundo de objetos.
        """
        return Libro(
            isbn=fila["isbn"],
            titulo=fila["titulo"],
            autor=fila["autor"],
            genero=fila["genero"],
            stock=fila["stock"]
        )