from datetime import date


class Campania:

    def __init__(self, nombre: str, fecha_inicio: date, fecha_termino: date):
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, new_nombre) -> None:
        self.__nombre = new_nombre

    def __str__(self):
        return f"""
        Nombre de la campaña
        """
