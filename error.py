class Error(Exception):
    pass


class SubTipoInvalidoError(Error):

    def __init__(self, mensaje):
        self.mensaje = mensaje

    def __str__(self) -> str:
        return super().__str__()


class LargoExcedidoError(Error):
    def __init__(self, mensaje):
        self.mensaje = mensaje
