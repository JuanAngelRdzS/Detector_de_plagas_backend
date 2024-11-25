from django.urls import path
from .import views

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

]
