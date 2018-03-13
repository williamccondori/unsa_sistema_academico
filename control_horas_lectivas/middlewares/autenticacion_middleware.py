from django.shortcuts import redirect

class AutenticacionMiddleware(object):
    def process_request(self, request):
        if not (request.session.get('username', False) or request.session.get('password', False)):
            print('No ha iniciado sesion')
            return redirect('/administracion/seguridad')

        return None