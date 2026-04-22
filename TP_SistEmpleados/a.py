from abc import ABC, abstractmethod

# Clase abstracta
class Empleado(ABC):
    def _init_(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    def mostrar_info(self):
        print(f"Empleado: {self.nombre}")
        print(f"Salario base: ${self.salario_base}")

    @abstractmethod
    def calcular_salario(self):
        pass


class EmpleadoTiempoCompleto(Empleado):
    def calcular_salario(self):
        return self.salario_base


class EmpleadoPorHora(Empleado):
    def _init_(self, nombre, salario_base, horas_trabajadas):
        super()._init_(nombre, salario_base)
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario(self):
        return self.salario_base * self.horas_trabajadas



class EmpleadoComision(Empleado):
    def _init_(self, nombre, salario_base, ventas, porcentaje):
        super()._init_(nombre, salario_base)
        self.ventas = ventas
        self.porcentaje = porcentaje

    def calcular_salario(self):
        return self.salario_base + (self.ventas * self.porcentaje)


class EmpleadoFreelance(Empleado):
    def _init_(self, nombre, salario_base, proyectos):
        super()._init_(nombre, salario_base)
        self.proyectos = proyectos

    def calcular_salario(self):
        return self.salario_base * self.proyectos


e1 = EmpleadoTiempoCompleto("Juan", 100000)
e2 = EmpleadoPorHora("Ana", 2000, 40)
e3 = EmpleadoComision("Luis", 50000, 200000, 0.1)
e4 = EmpleadoFreelance("Sofi", 15000, 3)

empleados = [e1, e2, e3, e4]

print("=== LISTA DE EMPLEADOS ===")

for empo in empleados:
    print("\n----------------------")
    empo.mostrar_info()
    salario = empo.calcular_salario()
    print(f"Salario final: ${salario}")