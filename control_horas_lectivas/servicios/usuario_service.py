from control_horas_lectivas.models import UserSystem
from control_horas_lectivas.dtos.usuario_dto import UsuarioDto

class UsuarioService():
    def login(self, username, password):
        usuario = UserSystem.objects.filter(username=username)
        if len(usuario) is 0:
            raise ValueError('Usuario incorrecto!')
        usuario = usuario[0]
        """
        print(usuario.user.password)
        if not usuario.user.password == password:
           raise ValueError('Contraseña incorrecto!')
        """
        usuario_dto = UsuarioDto(
            usuario.username,
            usuario.departament.id
        )
        return usuario_dto
        
        
        