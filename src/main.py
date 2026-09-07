# src/main.py
from dominio.empleado import Empleado
from dominio.proyecto import Proyecto

empleado = Empleado(
    nombre = "Ana Torres",
    correo = "ana.torres@ecotech.cl"
)

proyecto = Proyecto(
    nombre = "Software de comercio",
    cantidad_empleados = 7,
    departamento = "Marketing"
)

print(empleado.mostrar_datos())
print(proyecto.mostrar_datos2())

