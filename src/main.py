# src/main.py
from datetime import date
from dominio.departamento import Departamento
from dominio.empleado import Empleado
from dominio.proyecto import Proyecto
from dominio.registrotiempo import RegistroTiempo
from persistencia.crear_bd import crear_tablas
from dominio.empleado import Empleado
from persistencia.empleado_dao import EmpleadoDAO


crear_tablas()
empleado = Empleado(nombre="Ana Pérez", direccion="Pasaje Cielo 2023", numero_telefono=947583921,
                    correo="ana@ecotech.cl", fecha_contrato="20 de abril del 2024", sueldo=350000.34, rol=1)

print("Antes:", empleado._id)
# None

EmpleadoDAO.insertar(empleado)

print("Después:", empleado._id)
# id generado por la BD

empleado = Empleado(
    nombre="Javier Castillo",
    direccion="calle hurtado 2026",
    numero_telefono=973382653,
    correo="javier.castillo@ecotech.cl",
    fecha_contrato="09 de mayo del 2021",
    sueldo=389000.94,
    rol=2
)

EmpleadoDAO.insertar(empleado)

encontrado = EmpleadoDAO.buscar_por_id(empleado._id)
print("Encontrado:", encontrado)

print("Listado:")
for item in EmpleadoDAO.listar():
    print(item)