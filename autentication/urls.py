from venv import create
from .views import cadastro, login, index, inicialaluno, projeto_view, logout_view, cadastrar_projeto, editar_atividade, editar_projeto, excluir_atividade, excluir_projeto, cadastrar_atividade, inicialprofessor
from django.urls import	path

urlpatterns = [
    path('', index, name = 'index'),
    path('cadastro/', cadastro, name = 'cadastro'),
    path('login/', login, name = 'login'),
    path('inicialaluno', inicialaluno, name = 'inicialaluno'),
    path('projeto/<int:id>/', projeto_view, name = 'projeto'),
    path('logout', logout_view,  name = 'logout'),
    path('cadastrar_projeto', cadastrar_projeto, name = 'cadastrar_projeto'),
    path('cadastrar_atividade', cadastrar_atividade, name = 'cadastrar_atividade'),
    path('inicial_professor', inicialprofessor, name = 'inicialprofessor'),
    path('excluir_projeto/<int:id>/', excluir_projeto, name = 'excluir_projeto'),
    path('excluir_atividade/<int:id>/', excluir_atividade, name = 'excluir_atividade'),
    path('editar_projeto/<int:id>/', editar_projeto, name = 'editar_projeto'),
    path('editar_atividade/<int:id>/', editar_atividade, name = 'editar_atividade')
]