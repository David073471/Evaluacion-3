from django.contrib import admin
from .models import Pelicula, Critica

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)

@admin.register(Critica)
class CriticaAdmin(admin.ModelAdmin):
    list_display = ('pelicula', 'usuario', 'calificacion', 'fecha')
    list_filter = ('pelicula', 'calificacion')
    search_fields = ('usuario__username', 'pelicula__titulo')
