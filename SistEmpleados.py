from abc import ABC, abstractmethod

# ─────────────────────────────────────────
# CLASS BASE ABSTRACTA
# ─────────────────────────────────────────

class Empleado(ABC):
    #Clase abstracta que representa a cualquier empleado

    def __init__(self, nombre: str, salario_base: float):
        self.nombre = nombre
        self.salario_base = salario_base

    def mostrar_info(self) -> str:
        #Método concreto: todos los empleados lo comparten.
        return f"Empleado: {self.nombre} | Salario base: ${self.salario_base:,.2f}"

    @abstractmethod
    def calcular_salario(self) -> float:
        #Método abstracto: cada subclase define su propia lógica
        pass


# ─────────────────────────────────────────
# SUBCLASS 1 – Salario fijo mensual
# ─────────────────────────────────────────

class EmpleadoTiempoCompleto(Empleado):
    #Cobra exactamente el salario_base, sin variaciones

    def calcular_salario(self) -> float:
        return self.salario_base


# ─────────────────────────────────────────
# SUBCLASS 2 – Pago por horas trabajadas
# ─────────────────────────────────────────

class EmpleadoPorHora(Empleado):
    #Cobra según la cantidad de horas trabajadas ese mes

    def __init__(self, nombre: str, salario_base: float,
                 horas_trabajadas: int, valor_hora: float):
        super().__init__(nombre, salario_base)
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora

    def calcular_salario(self) -> float:
        return self.horas_trabajadas * self.valor_hora


# ─────────────────────────────────────────
# SUBCLASS 3 – Salario base + comisión
# ─────────────────────────────────────────

class EmpleadoComision(Empleado):
    #Cobra el salario base más un porcentaje sobre sus ventas

    def __init__(self, nombre: str, salario_base: float,
                 ventas_totales: float, porcentaje_comision: float):
        super().__init__(nombre, salario_base)
        self.ventas_totales = ventas_totales
        self.porcentaje_comision = porcentaje_comision  # ej: 0.10 = 10%

    def calcular_salario(self) -> float:
        comision = self.ventas_totales * self.porcentaje_comision
        return self.salario_base + comision
# ─────────────────────────────────────────
# SUBCLASS 4 – Freelance por proyectos
# ─────────────────────────────────────────

class EmpleadoFreelance(Empleado):
    #Cobra una tarifa fija por cada proyecto completado ese mes

    def __init__(self, nombre: str, salario_base: float,
                 proyectos_completados: int, tarifa_por_proyecto: float):
        super().__init__(nombre, salario_base)
        self.proyectos_completados = proyectos_completados
        self.tarifa_por_proyecto = tarifa_por_proyecto

    def calcular_salario(self) -> float:
        return self.proyectos_completados * self.tarifa_por_proyecto


# ─────────────────────────────────────────
# PROGRAMA PRINCIPAL
# ─────────────────────────────────────────

empleados = [
    EmpleadoTiempoCompleto("Ana García", 150_000),
    EmpleadoPorHora("Carlos López", 0, horas_trabajadas=120, valor_hora=800),
    EmpleadoComision("Lucía Méndez", 80_000, ventas_totales=500_000, porcentaje_comision=0.08),
    EmpleadoFreelance("Martín Ríos", 0, proyectos_completados=5, tarifa_por_proyecto=30_000),
]

print("=" * 50)
print("        LIQUIDACIÓN DE SUELDOS")
print("=" * 50)

for empleado in empleados:
    print(empleado.mostrar_info())
    print(f"  → Salario a cobrar: ${empleado.calcular_salario():,.2f}")
    print("-" * 50)
    
