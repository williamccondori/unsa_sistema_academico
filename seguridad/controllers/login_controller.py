from django.views.generic import View

from django.shortcuts import render, redirect

class LoginController(View):

    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if (request.session.get('username', False) or request.session.get('password', False)):
            del request.session["username"]
            del request.session["password"]
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):        
        username = str(request.POST['username'])
        password = str(request.POST['password'])

        if username == 'william':
            if password == 'Computo.123':
                print('Se esta iniciando sesion')
                request.session["username"] = username
                request.session["password"] = password
                return redirect('/administracion/control_horas_lectivas')
            else:
                pass
        else:
            pass
        return render(request, self.template_name)