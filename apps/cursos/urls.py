from django.urls import path
from . import views

app_name = 'cursos'

urlpatterns = [
    path('', views.list_cursos, name='list_cursos'),
    path('adicionar/', views.add_curso, name='add_curso'),
    path('editar/<int:id_curso>/', views.edit_curso, name='edit_curso'),
    path('excluir/<int:id_curso>/', views.delete_curso, name='delete_curso'),
]