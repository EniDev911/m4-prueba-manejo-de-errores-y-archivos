class Anuncio:

    SUB_TIPOS = ()

    @staticmethod
    def validar_dimension(dimension):
        return dimension if dimension > 0 else 1

    @staticmethod
    def mostrar_formatos():
        print("FORMATO")
        print("=======")

    def __init__(self, alto, ancho):
        self.__alto = self.validar_dimension(alto)
        self.__ancho = self.validar_dimension(ancho)
        self.__url_archivo = ""
        self.__url_clic = ""
        self.__subtipo = ""

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, dimension: int):
        self.__alto = self.validar_dimension(dimension)

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, dimension):
        self.__ancho = self.validar_dimension(dimension)

    @property
    def url_archivo(self) -> str:
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, url_archivo):
        self.__url_archivo = url_archivo

    @property
    def url_clic(self) -> str:
        return self.__url_clic

    @url_clic.setter
    def url_archivo(self, url_clic):
        self.__url_clic = url_clic


class Display:
    FORMATO = "Display"
    SUB_TIPO = ("tradicional", "nativa")

    def comprimir_anuncio():
        pass

    def redimensionar_anuncio():
        pass


class Video:
    FORMATO = "Video"
    SUB_TIPO = ("instream", "outstream")

    @staticmethod
    def validar_duracion(duracion):
        if duracion > 0:
            return duracion
        else:
            return 5

    def __init__(self, duracion):
        self.__ancho = 1
        self.__alto = 1
        self.__duracion = self.validar_duracion(duracion)

    def comprimir_anuncio():
        pass

    def redimensionar_anuncio():
        pass

    @property
    def ancho(self):
        return self.__ancho

    @property
    def alto(self):
        return self.__alto

    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, duracion):
        self.__duracion = self.validar_duracion(duracion)


if __name__ == "__main__":
    a = Anuncio(-1, 100)
    print(a.alto)
    print(a.ancho)
