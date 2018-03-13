from django.views.generic import View

from django.shortcuts import render

class EscuelaController(View):

    template_name = 'escuela.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)