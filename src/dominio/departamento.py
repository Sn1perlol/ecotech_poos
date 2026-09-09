from dominio.empleado import Empleado


class Departamentos:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self._empleados: list[Empleado] = []

    def agregar_empleados(self, empleado: Empleado) -> bool:
        if empleado in self._empleados:
            return False

        self._empleados.append(empleado)
        return True
    @property
    def empleados(self) -> tuple:
        return tuple(self._empleados)

    def cantidad_empleados(self) -> int:
        return len(self._empleados)
