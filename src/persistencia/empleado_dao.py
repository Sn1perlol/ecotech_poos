from persistencia.conexion import abrir_conexion, obtener_motor, marcador_sql
from dominio.empleado import Empleado

class EmpleadoDAO:
    @staticmethod
    def insertar(empleado):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marcador = "?" if obtener_motor() == "sqlite" else "%s"

        sql = f"""
            INSERT INTO empleado (nombre, correo)
            VALUES ({marcador}, {marcador})
        """


        cursor.execute(sql, (empleado._nombre, empleado._correo))
        empleado._id = cursor.lastrowid
        conexion.commit()
        conexion.close()
        return empleado
    
    @staticmethod
    def actualizar(empleado)
        conexion = abrir_conexion()
        cursor = conexion.cursor()

        marca = marcador_sql()
        sql = (
            "UPDATE empleado"
            f"""SET nombre = {marca}, correo = {marca}, direccion = {marca},
                numero_telefono = {marca}, fecha_contrato = {marca}, sueldo = {marca},
                rol = {marca}"""
            f"WHERE id = {marca}"
        )

        cursor.execute(
            sql,
            (
                empleado.nombre,
                empleado.correo,
                empleado.direccion,
                empleado.numero_telefono,
                empleado.fecha_contrato,
                empleado.sueldo,
                empleado.rol,
                empleado.id
            )
        )

        conexion.commit()
        filas_afectadas = cursor.rowcount
        conexion.close()

        return filas_afectadas > 0
    
    @staticmethod
    def eliminar(id_empleado)
        conexion = abrir_conexion()
        cursor = conexion.cursor()

        marca = marcador_sql()
        sql = (
            "DELETE FROM empleado "
            f"WHERE id = {marca}"
        )

        cursor.execute(sql, (id_empleado,))
        conexion.commit()

        eliminado = cursor.rowcount > 0

        conexion.close()
        return eliminado

    @staticmethod
    def buscar_por_id(id):
        conexion = abrir_conexion()
        cursor = conexion.cursor()

        marca = marcador_sql()
        sql = f"""
                SELECT id, nombre, correo, direccion, numero_telefono,
                fecha_contrato, sueldo, rol
                FROM empleado WHERE id = {marca}
            """
        
        cursor.execute(sql, (id,))
        fila = cursor.fetchone()
        conexion.close()

        if fila is None:
            return None
        return EmpleadoDAO._fila_a_empleado(fila)


    @staticmethod
    def listar():
        conexion = abrir_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            """
                SELECT id, nombre, correo, direccion, numero_telefono,
                fecha_contrato, sueldo, rol
                FROM empleado
            """
        )
        filas = cursor.fetchall()
        conexion.close()

        empleados = []

        for fila in filas:
            empleados.append(EmpleadoDAO._fila_a_empleado(fila))
        return empleados
    
    @staticmethod
    def _fila_a_empleado(fila):
        return Empleado(
            id=fila[0],
            nombre=fila[1],
            correo=fila[2], 
            direccion="calle hurtado 2026",
            numero_telefono=973382653,
            fecha_contrato="09 de mayo del 2021",
            sueldo=389000.94,
            rol=2
        )