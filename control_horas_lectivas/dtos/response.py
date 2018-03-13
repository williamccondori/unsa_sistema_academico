class Response(object):

    def __init__(self, estado = True, mensaje = "Correcto", datos = None):
        self.Estado = estado
        self.Mensaje = mensaje
        self.Datos = datos
