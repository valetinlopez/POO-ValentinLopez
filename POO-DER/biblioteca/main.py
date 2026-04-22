from models.libro import Libro
from models.usuario import Usuario
from database.queries import insertar_usuario, insertar_libro, registrar_prestamo


def main():
    # Crear objetos
    usuario = Usuario("Juan")
    libro = Libro("El Principito", "Antoine de Saint-Exupéry")

    # Guardar en BD
    user_id = insertar_usuario(usuario.mostrar_info())
    libro_id = insertar_libro("El Principito", "Antoine de Saint-Exupéry")

    usuario.set_id(user_id)
    libro.set_id(libro_id)

    print("Usuario guardado:", usuario.mostrar_info())
    print("Libro guardado:", libro.mostrar_info())

    # Registrar préstamo
    registrar_prestamo(usuario.get_id(), libro.get_id())

    print("Préstamo registrado en la base de datos")


if __name__ == "__main__":
    main()