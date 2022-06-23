from django.urls import path
from . import views

app_name = 'areadeconhecimento'

urlpatterns = [
    path('', views.list_areadeconhecimento, name='list_areadeconhecimento'),
    path('adicionar/', views.add_areadeconhecimento, name='add_areadeconhecimento'),
    path('editar/<int:id_areadeconhecimento>/', views.edit_areadeconhecimento, name='edit_areadeconhecimento'),
    path('excluir/<int:id_areadeconhecimento>/', views.delete_areadeconhecimento, name='delete_areadeconhecimento'),
]