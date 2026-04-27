#Sistema de Gestión de Empleados

Sistema de nómina empresarial desarrollado en Python que maneja
Diferentes tipos de empleados, calcula salarios automáticamente
y genera reportes detallados por departamento.

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
