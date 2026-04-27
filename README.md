#Sistema de Gestión de Empleados

Sistema de nómina empresarial desarrollado en Python que maneja
Diferentes tipos de empleados, calcula salarios automáticamente
y genera reportes detallados por departamento.

## Demo
REPORTE DE NÓMINA — TechCorp Colombia
📁 TECNOLOGÍA (3 empleados)
[G001] Carlos Pérez | Gerente | Dpto: Tecnología | Salario: $10,000,000 COP
[E001] Luis Torres | Empleado Fijo | Dpto: Tecnología | Salario: $4,500,000 COP
[E002] María López | Por Horas | Dpto: Tecnología | Salario: $7,200,000 COP
────────────────────────────────────────
Subtotal: $21,700,000 COP
📁 VENTAS (3 empleados)
[G002] Ana García | Gerente | Dpto: Ventas | Salario: $9,000,000 COP
[E003] Pedro Ruiz | Empleado Fijo | Dpto: Ventas | Salario: $3,200,000 COP
[E004] Sofía Castro | Por Horas | Dpto: Ventas | Salario: $4,900,000 COP
────────────────────────────────────────
Subtotal: $17,100,000 COP
============================================================
NÓMINA TOTAL: $38.800.000 COP
EMPLEADOS:    6

## Características

- Tres tipos de empleados con cálculo de salario independiente
- Gerentes con bono porcentual configurable y gestión de equipos
- Empleados por horas con registro acumulativo de horas trabajadas
- Reporte de nómina agrupado por departamento con subtotales
- Búsqueda de empleados por código
- Filtrado por departamento

## Tipos de empleados

| Tipo | Cálculo de salario |
|---|---|
| Empleado Fijo | Salario base mensual fijo |
| Empleado Por Horas | Tarifa por hora × horas trabajadas en el mes |
| Gerente | Salario base × (1 + bono porcentual) |

## Instalación

```bash
# No requiere librerías externas — solo Python 3.10+
python empleados.py
```

## Cómo usarlo

```python
from empleados import EmpleadoFijo, EmpleadoPorHoras, Gerente, GestorEmpleados

# Crear la empresa
empresa = GestorEmpleados("Mi Empresa")

# Crear empleados
gerente = Gerente("Carlos Pérez", "G001", "Tecnología", 8_000_000, 0.25)
desarrollador = EmpleadoFijo("Luis Torres", "E001", "Tecnología", 4_500_000)
freelancer = EmpleadoPorHoras("María López", "E002", "Tecnología", 45_000)

# Registrar horas del freelancer
freelancer.registrar_horas(160)

# Armar equipo del gerente
gerente.agregar_al_equipo(desarrollador)
gerente.agregar_al_equipo(freelancer)

# Agregar a la empresa
empresa.agregar(gerente)
empresa.agregar(desarrollador)
empresa.agregar(freelancer)

# Ver reporte completo
empresa.reporte()
```

## Autor

**Veronika Koral**
GitHub: @Rinnendothir
https://github.com/Rinnendothir
