from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from usuarios import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # login en "/"
    path('admin/', admin.site.urls),
    path('cine/', views.cine, name='cine'),
    path('criticar/<int:pelicula_id>/', views.hacer_critica, name='hacer_critica'),
    path('logout/', views.cerrar_sesion, name='logout'),  # Usamos nuestra propia vista para logout
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
