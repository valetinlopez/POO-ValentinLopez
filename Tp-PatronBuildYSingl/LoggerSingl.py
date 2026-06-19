"""
TP - Patrón Singleton
Sistema de logs para una aplicación bancaria.

El patrón Singleton garantiza que una clase tenga UNA SOLA instancia
en toda la ejecución del programa, y provee un punto de acceso global
a ella. Acá lo aplicamos para que todos los servicios (login,
transferencias, consultas, etc.) escriban en el MISMO logger.
"""

from __future__ import annotations
from datetime import datetime
from typing import Optional


# --------------------------------------------------------------------------
# Singleton: Logger
# --------------------------------------------------------------------------
class Logger:
    """Logger Singleton de la aplicación bancaria.

    Implementación basada en sobrescribir __new__: cada vez que alguien
    intenta crear un Logger() con `Logger()`, en realidad recibe siempre
    la misma instancia ya creada (si existe).
    """

    _instancia: Optional["Logger"] = None

    def __new__(cls) -> "Logger":
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._inicializado = False
        return cls._instancia

    def __init__(self) -> None:
        # Evita que __init__ vuelva a resetear el estado en cada
        # Logger() posterior, ya que __init__ se ejecuta siempre,
        # incluso cuando __new__ devuelve la instancia ya existente.
        if self._inicializado:
            return
        self._historial: list[str] = []
        self._inicializado = True

    def log(self, mensaje: str) -> None:
        """Registra un mensaje con nivel INFO y timestamp."""
        linea = f"[INFO] {mensaje}"
        self._historial.append(linea)
        print(linea)

    def ver_historial(self) -> list[str]:
        """Devuelve todos los mensajes registrados hasta el momento."""
        return list(self._historial)


# --------------------------------------------------------------------------
# Servicios que consumen el Logger (todos comparten la misma instancia)
# --------------------------------------------------------------------------
class LoginService:
    def __init__(self) -> None:
        self.logger = Logger()

    def iniciar_sesion(self, usuario: str) -> None:
        self.logger.log(f"Usuario {usuario} inició sesión")

    def cerrar_sesion(self, usuario: str) -> None:
        self.logger.log(f"Usuario {usuario} cerró sesión")


class TransferService:
    def __init__(self) -> None:
        self.logger = Logger()

    def transferir(self, monto: float) -> None:
        self.logger.log(f"Transferencia realizada por ${monto:,.0f}")


class AccountService:
    def __init__(self) -> None:
        self.logger = Logger()

    def consultar_saldo(self) -> None:
        self.logger.log("Consulta de saldo realizada")


# --------------------------------------------------------------------------
# Cliente: simulación de uso
# --------------------------------------------------------------------------
def main() -> None:
    login_service = LoginService()
    transfer_service = TransferService()
    account_service = AccountService()

    login_service.iniciar_sesion("Valen")
    transfer_service.transferir(50000)
    account_service.consultar_saldo()
    login_service.cerrar_sesion("fede")

    print()
    print("¿Las 3 instancias de Logger son la misma? ->",
          login_service.logger is transfer_service.logger is account_service.logger)
    print("id(login_service.logger):   ", id(login_service.logger))
    print("id(transfer_service.logger):", id(transfer_service.logger))
    print("id(account_service.logger): ", id(account_service.logger))


if __name__ == "__main__":
    main()