class InformacionDto(object):

    def __init__(self, id=0, nombre='', cargo='', imagen=''
        , nombre_departamento='', nombre_plan_estudio='', username=''):
        self.Id = id
        self.Username = username
        self.Nombre = nombre
        self.Cargo = cargo
        self.Imagen = imagen
        self.NombreDepartamento = nombre_departamento
        self.NombrePlanEstudio = nombre_plan_estudio  
    