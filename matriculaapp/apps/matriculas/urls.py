from django.urls import path
from . import views

app_name = 'matriculas'

urlpatterns = [
    path('', views.list_matriculas, name='list_mastriculas'),
    path('adicionar/<int:id_aluno>/', views.add_matricula, name='add_matricula'),
    path('excluir/<int:id_matricula>/', views.delete_matricula, name='delete_matricula'),
    path('excluir-item/<int:id_matricula_item>/', views.delete_matricula_item, name='delete_matricula_item'),
    path('adicionar-item/<int:id_matricula>/', views.add_matricula_item, name='add_matricula_item'),
    path('editar-status/<int:id_matricula>/', views.edit_matricula_status, name='edit_matricula_status'),
]