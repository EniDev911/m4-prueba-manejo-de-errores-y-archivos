from datetime import date, datetime
from error import LargoExcedidoError
from anuncio import Display, Video, Social


class Campania:

    def __init__(
        self, nombre: str, fecha_inicio: date, fecha_termino: date, anuncios: tuple
    ) -> None:
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = [self.__crear_anuncio(anuncio) for anuncio in anuncios]

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre) -> None:
        if len(nombre) <= 250:
            self.__nombre = nombre
        else:
            raise LargoExcedidoError(250)

    @property
    def fecha_inicio(self) -> date:
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    @property
    def fecha_termino(self) -> date:
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, fecha_termino):
        self.__fecha_termino = fecha_termino

    def __crear_anuncio(self, anuncio):

        datos_filtrados = {k: v for k, v in anuncio.items() if k != "tipo"}

        if anuncio["tipo"] == "video":
            return Video(**datos_filtrados)
        elif anuncio["tipo"] == "display":
            return Display(**datos_filtrados)
        elif anuncio["tipo"] == "social":
            return Social(**datos_filtrados)
        else:
            print("Tipo de Anuncio no existe o no es válido.")

    def __mostrar_campania(self):
        print(f"Campaña {self.nombre} creada. con los siguientes anuncios:")
        print()
        for anuncio in self.__anuncios:
            anuncio.mostrar_formatos(anuncio.FORMATO, anuncio.SUB_TIPOS)

    def __str__(self):
        return f"{self.__mostrar_campania()}"


if __name__ == "__main__":
    anuncios = (
        {
            "alto": 1600,
            "ancho": 1400,
            "url_archivo": "C:\\path\\to\\display1",
            "url_clic": "\\path\\to\\clic_display",
            "subtipo": "tradicional",
            "tipo": "display",
        },
        {
            "alto": 1600,
            "ancho": 1400,
            "url_archivo": "C:\\path\\to\\social.png",
            "url_clic": "\\path\\to\\social",
            "subtipo": "linkedin",
            "tipo": "social",
        },
        {
            "url_archivo": "C:\\path\\to\\display1",
            "url_clic": "\\path\\to\\clic_display",
            "subtipo": "instream",
            "duracion": 10,
            "tipo": "video",
        },
    )

    fecha_inicio = datetime.strptime("21/06/2024", "%d/%m/%Y")
    fecha_termino = datetime.strptime("29/06/2024", "%d/%m/%Y")
    nueva_campania = Campania("Nueva campaña", fecha_inicio, fecha_termino, anuncios)
    print(nueva_campania)
