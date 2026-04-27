from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime

class Empleado(ABC):
    def __init__(self, nombre: str, codigo: str, departamento: str):
        self.nombre = nombre
        self.codigo = codigo
        self.departamento = departamento
        self.fecha_ingreso = datetime.now().strftime("%Y-%m-%d")
        self.activo = True

    @abstractmethod
    def calcular_salario(self) -> float:
        """Cada tipo de empleado calcula su salario diferente."""
        pass

    @abstractmethod
    def tipo(self) -> str:
        """Retorna el tipo de empleado."""
        pass

    def info(self) -> str:
        return (f"[{self.codigo}] {self.nombre} | "
        f"{self.tipo()} | "
        f"Dpto: {self.departamento} | "
        f"Salario: ${self.calcular_salario():,.0f} COP")
    
    def __str__(self) -> str:
        return self.info()


class EmpleadoFijo(Empleado):
    """Empleado con salario fijo mensual."""

    def __init__(self, nombre: str, codigo: str,
                departamento: str, salario_base: float):
        super().__init__(nombre, codigo, departamento)
        self.salario_base = salario_base

    def tipo(self) -> str:
        return "Empleado Fijo"

    def calcular_salario(self) -> float:
        return self.salario_base
class EmpleadoPorHoras(Empleado):
    """Empleado que cobra por horas trabajadas."""

    def __init__(self, nombre: str, codigo: str,
                departamento: str, tarifa_hora: float,
    horas_mes: float = 0):
        super().__init__(nombre, codigo, departamento)
        self.tarifa_hora = tarifa_hora
        self.horas_mes = horas_mes

    def tipo(self) -> str:
        return "Por horas"

    def registrar_horas(self, horas: float) -> None:
        if horas < 0:
            raise ValueError("Las horas no pueden ser negativas")
        self.horas_mes += horas
        print(f"{self.nombre}: {horas}h registradas "
        f"(total mes: {self.horas_mes}h)")

    def calcular_salario(self) -> float:
        return self.tarifa_hora * self.horas_mes

class Gerente(EmpleadoFijo):
    """Gerent con salario fijo más bono por desempeño."""

    def __init__(self, nombre: str, codigo: str,
                departamento: str, salario_base: float,
    bono_porcentaje: float = 0.20):
        super().__init__(nombre, codigo, departamento, salario_base)
        self.bono_porcentaje = bono_porcentaje
        self.equipo: list = []
    def tipo(self) -> str:
        return "Gerente"

    def calcular_salario(self) -> float:
        return self.salario_base * (1 + self.bono_porcentaje)
        
    def agregar_al_equipo(self, empleado: Empleado) -> None:
        self.equipo.append(empleado)
        print(f"{empleado.nombre} agregado al equipo")

    def info_equipo(self) -> str:
        if not self.equipo:
            return f"{self.nombre} no tiene equipo asignado"
        miembros = "\n  ".join(e.nombre for e in self.equipo)
        return f"Equipo de {self.nombre}:\n   {miembros}"

class GestorEmpleados:
    def __init__(self, empresa: str):
        self.empresa = empresa
        self.empleados: list[Empleado] = []

    def agregar(self, empleado: Empleado) -> None:
        self.empleados.append(empleado)
        print(f"✅ {empleado.nombre} ({empleado.tipo()}) agregado")

    def buscar(self, codigo: str) -> Empleado | None:
        for emp in self.empleados:
            if emp.codigo == codigo:
                return emp
        return None

    def por_departamento(self, dpto: str) -> list:
        return [e for e in self.empleados
                if e.departamento.lower() == dpto.lower()]

    def nomina_total(self) -> float:
        return sum(e.calcular_salario() for e in self.empleados
                   if e.activo)

    def reporte(self) -> None:
        print(f"\n{'='*60}")
        print(f"  REPORTE DE NÓMINA — {self.empresa}")
        print(f"{'='*60}")

        dptos = set(e.departamento for e in self.empleados)
        for dpto in sorted(dptos):
            emps = self.por_departamento(dpto)
            total_dpto = sum(e.calcular_salario() for e in emps)
            print(f"\n {dpto.upper()} ({len(emps)} empleados)")
            for emp in emps:
                print(f"    {emp}")
            print(f"    {'─'*40}")
            print(f"    Subtotal: ${total_dpto:,.0f} COP")

        print(f"\n{'='*60}")
        print(f"  NÓMINA TOTAL: ${self.nomina_total():,.0f} COP")
        print(f"  EMPLEADOS:    {len(self.empleados)}")
        print(f"{'='*60}\n")


if __name__ == "__main__":
    empresa = GestorEmpleados("TechCorp Colombia")


    gerente_tech = Gerente("Carlos Pérez", "G001",
                           "Tecnología", 8_000_000, 0.25)
    gerente_ventas = Gerente("Ana García", "G002",
                             "Ventas", 7_500_000, 0.20)

    dev1 = EmpleadoFijo("Luis Torres", "E001",
                        "Tecnología", 4_500_000)
    dev2 = EmpleadoPorHoras("María López", "E002",
                            "Tecnología", 45_000)
    vendedor1 = EmpleadoFijo("Pedro Ruiz", "E003",
                             "Ventas", 3_200_000)
    vendedor2 = EmpleadoPorHoras("Sofía Castro", "E004",
                                 "Ventas", 35_000)


    dev2.registrar_horas(160)    
    vendedor2.registrar_horas(140)

  
    gerente_tech.agregar_al_equipo(dev1)
    gerente_tech.agregar_al_equipo(dev2)
    gerente_ventas.agregar_al_equipo(vendedor1)
    gerente_ventas.agregar_al_equipo(vendedor2)


    for emp in [gerente_tech, gerente_ventas,
                dev1, dev2, vendedor1, vendedor2]:
        empresa.agregar(emp)


    empresa.reporte()

    print(gerente_tech.info_equipo())