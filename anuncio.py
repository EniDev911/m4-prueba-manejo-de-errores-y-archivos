from error import SubTipoInvalidoError


class Anuncio:
    FORMATO = ""
    SUB_TIPOS = ()

    @staticmethod
    def validar_dimension(dimension):
        return dimension if dimension > 0 else 1

    @staticmethod
    def mostrar_formatos(formato: str, subtipos: tuple):
        print("{}:".format(formato))
        print("=======")
        for subtipo in subtipos:
            print("-", subtipo)

    def __init__(self, alto, ancho, url_archivo, url_clic, subtipo):
        self.__alto = self.validar_dimension(alto)
        self.__ancho = self.validar_dimension(ancho)
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        if subtipo in self.SUB_TIPOS:
            self.__sub_tipo = subtipo
        else:
            raise SubTipoInvalidoError(self.SUB_TIPOS)

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
    def sub_tipo(self):
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, subtipo):
        if subtipo in self.SUB_TIPOS:
            self.__sub_tipo = subtipo
        else:
            print("Excepcion")

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

    def comprimir_anuncio(self):
        pass

    def redimensionar_anuncio(self):
        pass


class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    @staticmethod
    def validar_duracion(duracion):
        return duracion if duracion > 0 else 5

    def __init__(self, url_archivo, url_clic, subtipo, duracion):
        super().__init__(1, 1, url_archivo, url_clic, subtipo)
        self.__duracion = Video.validar_duracion(duracion)

    @property
    def duracion(self):
        return self.__duracion

    # Setters
    @duracion.setter
    def duracion(self, duracion):
        self.__duracion = Video.validar_duracion(duracion)

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")


if __name__ == "__main__":
    anuncio_video = Video("C:\\video.mp3", "C:\\clic", "instream", 10)
    print(anuncio_video.alto)
    print(anuncio_video.ancho)
    anuncio_video.mostrar_formatos(Video.FORMATO, Video.SUB_TIPOS)
    anuncio_video.comprimir_anuncio()
    # print(anuncio_video.sub_tipo)
