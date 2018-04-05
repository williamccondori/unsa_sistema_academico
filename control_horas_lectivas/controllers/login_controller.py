from django.views.generic import View
from django.shortcuts import render, redirect
from control_horas_lectivas.servicios.usuario_service import UsuarioService
from control_horas_lectivas.dtos.usuario_dto import UsuarioDto


class LoginController(View):

    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if request.session.get('username', False):
            del request.session["username"]
            if request.session.get('id_departamento', False):
                del request.session["id_departamento"]
            if request.session.get('id_plan_estudio', False):
                del request.session["id_plan_estudio"]
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):   
        try:
            usuario_service = UsuarioService()
            username = str(request.POST['username'])
            password = str(request.POST['password'])
            usuario = usuario_service.login(username, password)
            request.session["username"] = usuario.Username
            request.session["id_departamento"] = usuario.IdDepartamento
            return redirect('/administracion/control_horas_lectivas')
        except Exception as e:
            return render(request, self.template_name)


        
