from django import forms
from .models import Critica

class CriticaForm(forms.ModelForm):
    class Meta:
        model = Critica
        fields = ['calificacion', 'comentario']
        widgets = {
            'calificacion': forms.Select(choices=[(i, f'{i} estrellas') for i in range(1, 6)]),
            'comentario': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escribe tu opinión...'})
        }
