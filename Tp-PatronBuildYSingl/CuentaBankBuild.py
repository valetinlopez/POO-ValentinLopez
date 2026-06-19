"""
TP 1 - Patrón Builder
Sistema de generación de cuentas bancarias.

El patrón Builder permite construir objetos complejos paso a paso,
evitando constructores con muchos parámetros (telescoping constructor)
y permitiendo crear distintas configuraciones del mismo objeto de
forma legible y encadenable (fluent interface).
"""

from __future__ import annotations
from enum import Enum
from typing import Optional


# --------------------------------------------------------------------------
# Enums para evitar "magic strings" y errores de tipeo
# --------------------------------------------------------------------------
class TipoCuenta(Enum):
    CAJA_AHORRO = "Caja de Ahorro"
    CUENTA_CORRIENTE = "Cuenta Corriente"


class Moneda(Enum):
    ARS = "ARS"
    USD = "USD"


# --------------------------------------------------------------------------
# Producto: la clase que queremos construir
# --------------------------------------------------------------------------
class CuentaBancaria:
    """Representa una cuenta bancaria con su configuración de servicios.

    No se instancia directamente con __init__ "público" lleno de
    parámetros: se construye a través de CuentaBancariaBuilder.
    """

    def __init__(self) -> None:
        # Valores por defecto; el Builder los va completando
        self.titular: str = ""
        self.dni: str = ""
        self.tipo_cuenta: Optional[TipoCuenta] = None
        self.moneda: Optional[Moneda] = None
        self.tarjeta_debito: bool = False
        self.chequera: bool = False
        self.home_banking: bool = False
        self.limite_extraccion: float = 0.0

    def __str__(self) -> str:
        lineas = [
            "=" * 45,
            "        CUENTA BANCARIA GENERADA",
            "=" * 45,
            f"Titular:              {self.titular}",
            f"DNI:                  {self.dni}",
            f"Tipo de cuenta:       {self.tipo_cuenta.value}",
            f"Moneda:               {self.moneda.value}",
            f"Tarjeta de débito:    {'Sí' if self.tarjeta_debito else 'No'}",
            f"Chequera:             {'Sí' if self.chequera else 'No'}",
            f"Home Banking:         {'Sí' if self.home_banking else 'No'}",
            f"Límite de extracción: ${self.limite_extraccion:,.2f}",
            "=" * 45,
        ]
        return "\n".join(lineas)


# --------------------------------------------------------------------------
# Builder: construye la CuentaBancaria paso a paso
# --------------------------------------------------------------------------
class CuentaBancariaBuilder:
    """Builder fluido para CuentaBancaria.

    Cada método "set_" devuelve self (self) para permitir encadenar
    llamadas (method chaining) y termina con build() que valida y
    entrega el objeto final.
    """

    def __init__(self) -> None:
        self._cuenta = CuentaBancaria()

    def con_titular(self, nombre: str) -> CuentaBancariaBuilder:
        self._cuenta.titular = nombre
        return self

    def con_dni(self, dni: str) -> CuentaBancariaBuilder:
        self._cuenta.dni = dni
        return self

    def con_tipo_cuenta(self, tipo: TipoCuenta) -> CuentaBancariaBuilder:
        self._cuenta.tipo_cuenta = tipo
        return self

    def con_moneda(self, moneda: Moneda) -> CuentaBancariaBuilder:
        self._cuenta.moneda = moneda
        return self

    def con_tarjeta_debito(self, valor: bool = True) -> CuentaBancariaBuilder:
        self._cuenta.tarjeta_debito = valor
        return self

    def con_chequera(self, valor: bool = True) -> CuentaBancariaBuilder:
        self._cuenta.chequera = valor
        return self

    def con_home_banking(self, valor: bool = True) -> CuentaBancariaBuilder:
        self._cuenta.home_banking = valor
        return self

    def con_limite_extraccion(self, monto: float) -> CuentaBancariaBuilder:
        self._cuenta.limite_extraccion = monto
        return self

    def build(self) -> CuentaBancaria:
        """Valida datos mínimos obligatorios y devuelve la cuenta final."""
        if not self._cuenta.titular:
            raise ValueError("La cuenta debe tener un titular.")
        if not self._cuenta.dni:
            raise ValueError("La cuenta debe tener un DNI.")
        if self._cuenta.tipo_cuenta is None:
            raise ValueError("La cuenta debe tener un tipo de cuenta.")
        if self._cuenta.moneda is None:
            raise ValueError("La cuenta debe tener una moneda.")
        return self._cuenta


# --------------------------------------------------------------------------
# Cliente: ejemplos de uso
# --------------------------------------------------------------------------
def main() -> None:
    # ---- Cliente básico ----
    cuenta_basica = (
        CuentaBancariaBuilder()
        .con_titular("Valentina Gómez")
        .con_dni("40123456")
        .con_tipo_cuenta(TipoCuenta.CAJA_AHORRO)
        .con_moneda(Moneda.ARS)
        .con_home_banking()
        .con_tarjeta_debito()
        .build()
    )
    print(cuenta_basica)
    print()

    # ---- Cliente premium ----
    cuenta_premium = (
        CuentaBancariaBuilder()
        .con_titular("Federico Alonso")
        .con_dni("35987654")
        .con_tipo_cuenta(TipoCuenta.CUENTA_CORRIENTE)
        .con_moneda(Moneda.USD)
        .con_home_banking()
        .con_tarjeta_debito()
        .con_chequera()
        .con_limite_extraccion(2_000_000)
        .build()
    )
    print(cuenta_premium)


if __name__ == "__main__":
    main()