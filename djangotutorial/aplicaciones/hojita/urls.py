from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('registrarUsuario/', views.registrarUsuario),
    path('editarUser/<IdUser>', views.editarUser),
    path('editaUser/<IdUser>', views.editaUser),  # Con parámetros
    path('borrarUser/<IdUser>', views.borrarUser),

    path('registrarPlaga/', views.registrarPlaga),
    path('editarPlaga/<IdPlaga>', views.editarPlaga),
    path('editaPlaga/<IdPlaga>', views.editaPlaga),
    path('borrarPlaga/<IdPlaga>', views.borrarPlaga),
    
    path('upload/', views.upload_image, name='upload_image'),
    path('csrf-token/', views.csrf_token),

]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
