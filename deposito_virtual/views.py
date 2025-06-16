# deposito_virtual/views.py

from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola desde views del proyecto")
