class Proyecto:
    def __init__(self, nombre: str, cantidad_empleados: int, departamento: str):
        self.nombre = nombre
        self.cantidad_empleados = cantidad_empleados
        self.departamento = departamento


    def mostrar_datos2(self) -> str:
        return f"{self.nombre} - {self.cantidad_empleados} - {self.departamento}"