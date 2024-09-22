class Error(Exception):
    pass


class SubTipoInvalidoError(Error):

    def __init__(self, subtipos):
        self.__sub_tipos = subtipos

    def __str__(self) -> str:
        return f"Subtipo Invalido, los Subtipos válidos son {self.__sub_tipos}"


class LargoExcedidoError(Error):
    def __init__(self, mensaje):
        self.mensaje = mensaje
