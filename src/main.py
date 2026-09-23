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
empleado = Empleado(nombre="Ana Pérez", correo="ana@ecotech.cl")
print("Antes:", empleado.id)
# None
EmpleadoDAO.insertar(empleado)
print("Después:", empleado.id)
# id generado por la BD

def main():
    print("=== SISTEMA DE GESTIÓN DE EMPLEADOS Y PROYECTOS ===\n")

    # 1. Crear un Departamento
    depto_sistemas = Departamento(101, "Sistemas", "G001")
    print(f"Creado: {depto_sistemas}")

    # 2. Crear Empleados
    empleado1 = Empleado(1, "Ana Gomez", "Calle Falsa 123", 5551234, "ana@mail.com", date(2023, 1, 15), 2500.0, 1)
    empleado2 = Empleado(2, "Carlos Ruiz", "Avenida Siempreviva 742", 5559876, "carlos@mail.com", date(2023, 3, 10), 2800.0, 2)
    
    # 3. Agregar empleados al departamento
    print("\n--- Agregando Empleados al Departamento ---")
    print(depto_sistemas.agregarEmpleado(empleado1))
    print(depto_sistemas.agregarEmpleado(empleado2))
    
    # 4. Crear un Proyecto
    print("\n--- Creando Proyecto ---")
    print(depto_sistemas.creacionProyecto("Desarrollo App Móvil"))
    
    # Obtenemos el proyecto recién creado
    proyecto_actual = depto_sistemas._proyectos[0]
    
    # 5. Asignar empleados al proyecto
    print("\n--- Asignando Empleados al Proyecto ---")
    print(proyecto_actual.asignarEmpleado(empleado1))
    print(proyecto_actual.asignarEmpleado(empleado2))
    
    # 6. Registrar horas trabajadas (Ahora usando RegistroTiempo)
    print("\n--- Registrando Horas Trabajadas ---")
    registro1 = RegistroTiempo(501, 8, date(2023, 10, 25), "Programación Backend", 15.0)
    registro2 = RegistroTiempo(502, 4, date(2023, 10, 26), "Reunión con Cliente", 15.0)
    
    empleado1.registrarHoras(registro1)
    empleado1.registrarHoras(registro2)
    
    # 7. Probar métodos de consulta
    print("\n--- Consultas Finales ---")
    print(f"Salario de {empleado1._nombre}: ${empleado1.verSalario()}")
    print(f"Horas registradas en el objeto RegistroTiempo: {registro1.calculoHoras()} hrs")
    print(f"Costo total del registro 1: ${registro1.calcular_costo_total()}")
    
    # Mostrar historial de tiempo de un empleado
    empleado1.ver_historial_tiempo()

    # 8. Desvincular empleado de un proyecto
    print("\n--- Desvinculando Empleado ---")
    print(proyecto_actual.desvincularEmpleado(empleado2))

if __name__ == "__main__":
    main()