# test_empleados.py

import pytest
from empleados import (EmpleadoFijo, EmpleadoPorHoras,
                       Gerente, GestorEmpleados)


# ── PRUEBAS DE EMPLEADO FIJO ─────────────────────────────
def test_empleado_fijo_salario():
    emp = EmpleadoFijo("Luis", "E001", "Tech", 4_500_000)
    assert emp.calcular_salario() == 4_500_000

def test_empleado_fijo_tipo():
    emp = EmpleadoFijo("Luis", "E001", "Tech", 4_500_000)
    assert emp.tipo() == "Empleado Fijo"

def test_empleado_fijo_atributos():
    emp = EmpleadoFijo("Luis", "E001", "Tech", 4_500_000)
    assert emp.nombre == "Luis"
    assert emp.codigo == "E001"
    assert emp.departamento == "Tech"
    assert emp.activo == True


# ── PRUEBAS DE EMPLEADO POR HORAS ───────────────────────
def test_empleado_horas_sin_horas():
    emp = EmpleadoPorHoras("María", "E002", "Tech", 45_000)
    assert emp.calcular_salario() == 0

def test_empleado_horas_con_horas():
    emp = EmpleadoPorHoras("María", "E002", "Tech", 45_000)
    emp.registrar_horas(160)
    assert emp.calcular_salario() == 7_200_000

def test_empleado_horas_acumulacion():
    emp = EmpleadoPorHoras("María", "E002", "Tech", 45_000)
    emp.registrar_horas(80)
    emp.registrar_horas(80)
    assert emp.horas_mes == 160

def test_empleado_horas_negativas_lanza_error():
    emp = EmpleadoPorHoras("María", "E002", "Tech", 45_000)
    with pytest.raises(ValueError):
        emp.registrar_horas(-5)


# ── PRUEBAS DE GERENTE ───────────────────────────────────
def test_gerente_salario_con_bono():
    gerente = Gerente("Carlos", "G001", "Tech", 8_000_000, 0.25)
    assert gerente.calcular_salario() == 10_000_000

def test_gerente_bono_defecto():
    gerente = Gerente("Carlos", "G001", "Tech", 8_000_000)
    # bono por defecto es 0.20
    assert gerente.calcular_salario() == 9_600_000

def test_gerente_agregar_equipo():
    gerente = Gerente("Carlos", "G001", "Tech", 8_000_000)
    emp = EmpleadoFijo("Luis", "E001", "Tech", 4_500_000)
    gerente.agregar_al_equipo(emp)
    assert len(gerente.equipo) == 1
    assert gerente.equipo[0].nombre == "Luis"

def test_gerente_equipo_vacio():
    gerente = Gerente("Carlos", "G001", "Tech", 8_000_000)
    assert "no tiene equipo" in gerente.info_equipo()


# ── PRUEBAS DEL GESTOR ───────────────────────────────────
def test_gestor_agregar_empleado():
    gestor = GestorEmpleados("TestCorp")
    emp = EmpleadoFijo("Luis", "E001", "Tech", 4_500_000)
    gestor.agregar(emp)
    assert len(gestor.empleados) == 1

def test_gestor_buscar_existente():
    gestor = GestorEmpleados("TestCorp")
    emp = EmpleadoFijo("Luis", "E001", "Tech", 4_500_000)
    gestor.agregar(emp)
    resultado = gestor.buscar("E001")
    assert resultado is not None
    assert resultado.nombre == "Luis"

def test_gestor_buscar_no_existente():
    gestor = GestorEmpleados("TestCorp")
    resultado = gestor.buscar("X999")
    assert resultado is None

def test_gestor_por_departamento():
    gestor = GestorEmpleados("TestCorp")
    gestor.agregar(EmpleadoFijo("Luis", "E001", "Tech", 4_500_000))
    gestor.agregar(EmpleadoFijo("Ana", "E002", "Ventas", 3_200_000))
    gestor.agregar(EmpleadoFijo("Pedro", "E003", "Tech", 4_000_000))
    tech = gestor.por_departamento("Tech")
    assert len(tech) == 2

def test_gestor_nomina_total():
    gestor = GestorEmpleados("TestCorp")
    gestor.agregar(EmpleadoFijo("Luis", "E001", "Tech", 4_500_000))
    gestor.agregar(EmpleadoFijo("Ana", "E002", "Ventas", 3_200_000))
    assert gestor.nomina_total() == 7_700_000

def test_gestor_nomina_excluye_inactivos():
    gestor = GestorEmpleados("TestCorp")
    emp1 = EmpleadoFijo("Luis", "E001", "Tech", 4_500_000)
    emp2 = EmpleadoFijo("Ana", "E002", "Ventas", 3_200_000)
    emp2.activo = False   # desactivar este empleado
    gestor.agregar(emp1)
    gestor.agregar(emp2)
    assert gestor.nomina_total() == 4_500_000  # solo cuenta emp1