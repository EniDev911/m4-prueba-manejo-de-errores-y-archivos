class Error(Exception):
    pass


class SubTipoInvalidoError(Error):

    def __init__(self, subtipos):
        self.__sub_tipos = subtipos

    def __str__(self) -> str:
        return f"Subtipo Invalido, los Subtipos válidos son {self.__sub_tipos}"


class LargoExcedidoError(Error):
    def __init__(self, longitud):
        self.__longitud = longitud

    def __str__(self) -> str:
        return f"Largo excedido, la cantidad máxima de caracteres es {self.__longitud}"
