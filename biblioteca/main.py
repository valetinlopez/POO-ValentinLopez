"""
main.py — Punto de entrada del sistema de gestión de biblioteca.

Responsabilidades:
  1. Inicializar la base de datos
  2. Instanciar los DAOs
  3. Instanciar los Services (inyectando los DAOs)
  4. Instanciar el Controller (inyectando los Services)
  5. Instanciar la Vista (inyectando el Controller)
  6. Arrancar el menú

Este es el único lugar donde todo se conecta.
Si mañana cambiamos SQLite por otro motor de base de datos,
solo cambia este archivo y los DAOs — nada más.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from dao.database import inicializar_db
from dao.libro_dao import LibroDAO
from dao.usuario_dao import UsuarioDAO
from dao.prestamo_dao import PrestamoDAO

from services.libro_service import LibroService
from services.usuario_service import UsuarioService
from services.prestamo_service import PrestamoService

from controller.biblioteca_controller import BibliotecaController
from view.menu import Menu

from domain.bibliotecario import Bibliotecario
from domain.admin import Admin


def main():
    # ── 1. Base de datos ──────────────────────────────────────────
    inicializar_db()

    # ── 2. DAOs ───────────────────────────────────────────────────
    libro_dao    = LibroDAO()
    usuario_dao  = UsuarioDAO()
    prestamo_dao = PrestamoDAO()

    # ── 3. Services ───────────────────────────────────────────────
    libro_svc    = LibroService(libro_dao)
    usuario_svc  = UsuarioService(usuario_dao)
    prestamo_svc = PrestamoService(prestamo_dao, libro_dao, usuario_dao)

    # ── 4. Empleado de sesión (en producción vendría de un login) ─
    empleado_sesion = Admin(
        id=1,
        nombre="Admin",
        apellido="Sistema",
        email="admin@biblioteca.com",
        legajo="ADM-001",
        salario=0,
        nivel_acceso=3
    )

    # ── 5. Controller ─────────────────────────────────────────────
    controller = BibliotecaController(
        libro_service=libro_svc,
        usuario_service=usuario_svc,
        prestamo_service=prestamo_svc,
        empleado_activo=empleado_sesion
    )

    # ── 6. Vista ──────────────────────────────────────────────────
    menu = Menu(controller)
    menu.mostrar()


if __name__ == "__main__":
    main()