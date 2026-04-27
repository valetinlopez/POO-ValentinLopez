import os
from controller.biblioteca_controller import BibliotecaController


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def separador(titulo=""):
    ancho = 55
    if titulo:
        print(f"\n{'─' * 4} {titulo} {'─' * (ancho - len(titulo) - 6)}")
    else:
        print("─" * ancho)


def pausar():
    input("\nPresioná Enter para continuar...")


def pedir_texto(mensaje, obligatorio=True):
    """Solicita un texto al usuario con validación básica."""
    while True:
        valor = input(f"  {mensaje}: ").strip()
        if valor:
            return valor
        if not obligatorio:
            return ""
        print("  ⚠ Este campo es obligatorio.")


def pedir_entero(mensaje, minimo=None):
    """Solicita un número entero con validación."""
    while True:
        try:
            valor = int(input(f"  {mensaje}: ").strip())
            if minimo is not None and valor < minimo:
                print(f"  ⚠ El valor mínimo es {minimo}.")
                continue
            return valor
        except ValueError:
            print("  ⚠ Ingresá un número válido.")


class Menu:
    """
    Capa Vista: muestra información y recibe input del usuario.
    Toda acción real la delega al controlador — nunca llama a los services.
    """

    def __init__(self, controller: BibliotecaController):
        self.__ctrl = controller

    # ================================================================
    # Menú principal
    # ================================================================

    def mostrar(self):
        empleado = self.__ctrl.obtener_empleado_activo()
        while True:
            limpiar_pantalla()
            print("╔═══════════════════════════════════════════════════╗")
            print("║          SISTEMA DE GESTIÓN BIBLIOTECA            ║")
            print("╠═══════════════════════════════════════════════════╣")
            print(f"║  Sesión: {empleado.nombre_completo():<41}║")
            print(f"║  Cargo:  {empleado.__class__.__name__:<41}║")
            print("╠═══════════════════════════════════════════════════╣")
            print("║                                                   ║")
            print("║   1. Gestión de libros                            ║")
            print("║   2. Gestión de usuarios                          ║")
            print("║   3. Préstamos y devoluciones                     ║")
            print("║   4. Reportes                                     ║")
            print("║   0. Salir                                        ║")
            print("║                                                   ║")
            print("╚═══════════════════════════════════════════════════╝")

            opcion = input("\n  Opción: ").strip()

            if opcion == "1":
                self.__menu_libros()
            elif opcion == "2":
                self.__menu_usuarios()
            elif opcion == "3":
                self.__menu_prestamos()
            elif opcion == "4":
                self.__menu_reportes()
            elif opcion == "0":
                print("\n  Hasta luego.\n")
                break
            else:
                print("  ⚠ Opción inválida.")
                pausar()

    # ================================================================
    # Submenú: Libros
    # ================================================================

    def __menu_libros(self):
        while True:
            limpiar_pantalla()
            separador("LIBROS")
            print("   1. Registrar libro")
            print("   2. Buscar por ISBN")
            print("   3. Buscar por título")
            print("   4. Ver catálogo completo")
            print("   5. Ver libros disponibles")
            print("   6. Eliminar libro")
            print("   0. Volver")
            separador()

            opcion = input("\n  Opción: ").strip()

            if opcion == "1":
                self.__registrar_libro()
            elif opcion == "2":
                self.__buscar_libro_isbn()
            elif opcion == "3":
                self.__buscar_libro_titulo()
            elif opcion == "4":
                self.__listar_libros()
            elif opcion == "5":
                self.__listar_disponibles()
            elif opcion == "6":
                self.__eliminar_libro()
            elif opcion == "0":
                break
            else:
                print("  ⚠ Opción inválida.")
                pausar()

    def __registrar_libro(self):
        separador("REGISTRAR LIBRO")
        try:
            isbn   = pedir_texto("ISBN")
            titulo = pedir_texto("Título")
            autor  = pedir_texto("Autor")
            genero = pedir_texto("Género")
            stock  = pedir_entero("Stock inicial", minimo=0)

            libro = self.__ctrl.registrar_libro(isbn, titulo, autor, genero, stock)
            print(f"\n  ✓ Libro registrado correctamente.")
            print(f"    {libro}")
        except Exception as e:
            print(f"\n  ✗ Error: {e}")
        pausar()

    def __buscar_libro_isbn(self):
        separador("BUSCAR POR ISBN")
        try:
            isbn  = pedir_texto("ISBN")
            libro = self.__ctrl.buscar_libro_por_isbn(isbn)
            print(f"\n  {libro}")
        except Exception as e:
            print(f"\n  ✗ {e}")
        pausar()

    def __buscar_libro_titulo(self):
        separador("BUSCAR POR TÍTULO")
        try:
            titulo    = pedir_texto("Título (parcial)")
            resultados = self.__ctrl.buscar_libros_por_titulo(titulo)
            if resultados:
                print(f"\n  Se encontraron {len(resultados)} resultado(s):\n")
                for libro in resultados:
                    print(f"    • {libro}")
            else:
                print("\n  No se encontraron libros.")
        except Exception as e:
            print(f"\n  ✗ {e}")
        pausar()

    def __listar_libros(self):
        separador("CATÁLOGO COMPLETO")
        libros = self.__ctrl.listar_libros()
        if libros:
            print(f"\n  Total: {len(libros)} libro(s)\n")
            for libro in libros:
                print(f"    • {libro}")
        else:
            print("\n  El catálogo está vacío.")
        pausar()

    def __listar_disponibles(self):
        separador("LIBROS DISPONIBLES")
        libros = self.__ctrl.listar_libros_disponibles()
        if libros:
            print(f"\n  Disponibles: {len(libros)} libro(s)\n")
            for libro in libros:
                print(f"    • {libro}")
        else:
            print("\n  No hay libros disponibles en este momento.")
        pausar()

    def __eliminar_libro(self):
        separador("ELIMINAR LIBRO")
        try:
            isbn = pedir_texto("ISBN del libro a eliminar")
            confirmacion = input(f"  ¿Confirmar eliminación? (s/n): ").strip().lower()
            if confirmacion == "s":
                self.__ctrl.eliminar_libro(isbn)
                print("\n  ✓ Libro eliminado correctamente.")
            else:
                print("\n  Operación cancelada.")
        except Exception as e:
            print(f"\n  ✗ Error: {e}")
        pausar()

    # ================================================================
    # Submenú: Usuarios
    # ================================================================

    def __menu_usuarios(self):
        while True:
            limpiar_pantalla()
            separador("USUARIOS / SOCIOS")
            print("   1. Registrar usuario")
            print("   2. Buscar por número de socio")
            print("   3. Ver todos los usuarios")
            print("   4. Dar de baja un usuario")
            print("   0. Volver")
            separador()

            opcion = input("\n  Opción: ").strip()

            if opcion == "1":
                self.__registrar_usuario()
            elif opcion == "2":
                self.__buscar_usuario()
            elif opcion == "3":
                self.__listar_usuarios()
            elif opcion == "4":
                self.__dar_de_baja()
            elif opcion == "0":
                break
            else:
                print("  ⚠ Opción inválida.")
                pausar()

    def __registrar_usuario(self):
        separador("REGISTRAR USUARIO")
        try:
            id_usr   = pedir_entero("ID de usuario", minimo=1)
            nombre   = pedir_texto("Nombre")
            apellido = pedir_texto("Apellido")
            email    = pedir_texto("Email")

            usuario = self.__ctrl.registrar_usuario(id_usr, nombre, apellido, email)
            print(f"\n  ✓ Usuario registrado. Número de socio asignado: #{usuario.nro_socio}")
            print(f"    {usuario.descripcion()}")
        except Exception as e:
            print(f"\n  ✗ Error: {e}")
        pausar()

    def __buscar_usuario(self):
        separador("BUSCAR USUARIO")
        try:
            nro = pedir_entero("Número de socio", minimo=1)
            u   = self.__ctrl.buscar_usuario(nro)
            print(f"\n  {u.descripcion()}")
        except Exception as e:
            print(f"\n  ✗ {e}")
        pausar()

    def __listar_usuarios(self):
        separador("TODOS LOS USUARIOS")
        usuarios = self.__ctrl.listar_usuarios()
        if usuarios:
            print(f"\n  Total: {len(usuarios)} usuario(s)\n")
            for u in usuarios:
                print(f"    • {u.descripcion()}")
        else:
            print("\n  No hay usuarios registrados.")
        pausar()

    def __dar_de_baja(self):
        separador("DAR DE BAJA")
        try:
            nro = pedir_entero("Número de socio", minimo=1)
            u   = self.__ctrl.buscar_usuario(nro)
            print(f"\n  Usuario encontrado: {u.nombre_completo()}")
            confirmacion = input("  ¿Confirmar baja? (s/n): ").strip().lower()
            if confirmacion == "s":
                self.__ctrl.dar_de_baja_usuario(nro)
                print("\n  ✓ Usuario dado de baja correctamente.")
            else:
                print("\n  Operación cancelada.")
        except Exception as e:
            print(f"\n  ✗ Error: {e}")
        pausar()

    # ================================================================
    # Submenú: Préstamos
    # ================================================================

    def __menu_prestamos(self):
        while True:
            limpiar_pantalla()
            separador("PRÉSTAMOS Y DEVOLUCIONES")
            print("   1. Realizar préstamo")
            print("   2. Registrar devolución")
            print("   3. Ver préstamos activos")
            print("   4. Historial de un usuario")
            print("   0. Volver")
            separador()

            opcion = input("\n  Opción: ").strip()

            if opcion == "1":
                self.__realizar_prestamo()
            elif opcion == "2":
                self.__registrar_devolucion()
            elif opcion == "3":
                self.__listar_activos()
            elif opcion == "4":
                self.__historial_usuario()
            elif opcion == "0":
                break
            else:
                print("  ⚠ Opción inválida.")
                pausar()

    def __realizar_prestamo(self):
        separador("NUEVO PRÉSTAMO")
        try:
            nro_socio = pedir_entero("Número de socio", minimo=1)
            isbn      = pedir_texto("ISBN del libro")

            prestamo = self.__ctrl.realizar_prestamo(nro_socio, isbn)
            print(f"\n  ✓ Préstamo realizado correctamente.")
            print(f"    {prestamo}")
            print(f"    Vence el: {prestamo.fecha_vencimiento}")
        except Exception as e:
            print(f"\n  ✗ Error: {e}")
        pausar()

    def __registrar_devolucion(self):
        separador("REGISTRAR DEVOLUCIÓN")
        try:
            id_prestamo = pedir_entero("ID del préstamo", minimo=1)
            prestamo    = self.__ctrl.registrar_devolucion(id_prestamo)
            print(f"\n  ✓ Devolución registrada correctamente.")
            print(f"    {prestamo}")
        except Exception as e:
            print(f"\n  ✗ Error: {e}")
        pausar()

    def __listar_activos(self):
        separador("PRÉSTAMOS ACTIVOS")
        prestamos = self.__ctrl.listar_prestamos_activos()
        if prestamos:
            print(f"\n  Activos: {len(prestamos)} préstamo(s)\n")
            for p in prestamos:
                alerta = "  ⚠ VENCIDO" if p.esta_vencido() else ""
                print(f"    • {p}{alerta}")
        else:
            print("\n  No hay préstamos activos.")
        pausar()

    def __historial_usuario(self):
        separador("HISTORIAL DE USUARIO")
        try:
            nro      = pedir_entero("Número de socio", minimo=1)
            historial = self.__ctrl.historial_usuario(nro)
            if historial:
                print(f"\n  {len(historial)} préstamo(s) en el historial:\n")
                for p in historial:
                    print(f"    • {p}")
            else:
                print("\n  Este usuario no tiene historial de préstamos.")
        except Exception as e:
            print(f"\n  ✗ {e}")
        pausar()

    # ================================================================
    # Submenú: Reportes
    # ================================================================

    def __menu_reportes(self):
        limpiar_pantalla()
        separador("REPORTES")

        vencidos = self.__ctrl.listar_prestamos_vencidos()
        activos  = self.__ctrl.listar_prestamos_activos()
        libros   = self.__ctrl.listar_libros()
        usuarios = self.__ctrl.listar_usuarios()

        print(f"\n  📚 Libros en catálogo:       {len(libros)}")
        print(f"  ✅ Préstamos activos:         {len(activos)}")
        print(f"  ⚠  Préstamos vencidos:        {len(vencidos)}")
        print(f"  👥 Usuarios registrados:      {len(usuarios)}")

        if vencidos:
            separador("PRÉSTAMOS VENCIDOS — REQUIEREN ATENCIÓN")
            for p in vencidos:
                print(f"    ⚠ {p}")

        pausar()