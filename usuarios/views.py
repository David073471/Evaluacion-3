from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Avg  # Para calcular el promedio
from .models import Pelicula, Critica

@login_required
def cine(request):
    query = request.GET.get('q', '')
    if query:
        peliculas = Pelicula.objects.filter(titulo__icontains=query)
    else:
        peliculas = Pelicula.objects.all()

    # Anotar el promedio de calificaciones
    peliculas = peliculas.annotate(promedio_calificacion=Avg('critica__calificacion'))

    return render(request, 'cine.html', {'peliculas': peliculas, 'query': query})

@login_required
def hacer_critica(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)

    if request.method == "POST":
        calificacion = int(request.POST.get('calificacion'))
        comentario = request.POST.get('comentario', '').strip()

        Critica.objects.create(
            usuario=request.user,
            pelicula=pelicula,
            calificacion=calificacion,
            comentario=comentario
        )
        return redirect('hacer_critica', pelicula_id=pelicula.id)

    criticas = Critica.objects.filter(pelicula=pelicula).order_by('-id')

    return render(request, 'criticas.html', {
        'pelicula': pelicula,
        'criticas': criticas
    })

def cerrar_sesion(request):
    logout(request)
    return redirect('login')
