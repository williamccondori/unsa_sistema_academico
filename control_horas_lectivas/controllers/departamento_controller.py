from django.views.generic import View

from django.shortcuts import render, redirect

class DepartamentoController(View):

    def post(self, request, *args, **kwargs):
        id_plan_estudio = request.session.get('id_plan_estudio', False)
        if id_plan_estudio is not False:
            del request.session['id_plan_estudio']    
        id_plan_estudio = str(request.POST['id_plan_estudio'])
        request.session['id_plan_estudio'] = id_plan_estudio
        return redirect('/administracion/control_horas_lectivas')