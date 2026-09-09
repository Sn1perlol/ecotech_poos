# src/main.py
from dominio.empleado import Empleado
from dominio.proyecto import Proyecto
from dominio.departamento import Departamentos


empleado_ana = Empleado(
    nombre = "Ana Torres",
    correo = "ana.torres@ecotech.cl"
)

proyecto = Proyecto(
    nombre = "Software de comercio",
    cantidad_empleados = 7,
    departamento = "Marketing"
)

desarrollo = Departamentos(
    nombre = "Departamento de Desarrollo"
)

desarrollo.agregar_empleados(empleado_ana)
print(desarrollo.cantidad_empleados())

for empleado in desarrollo.empleados:
    print(empleado.mostrar_datos())