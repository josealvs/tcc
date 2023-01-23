from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from django.shortcuts import HttpResponse, render, redirect
from .models import projetos, atividades
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator
from .forms import ProjetoForm, AtividadeForm

def index(request):
    return render(request, 'index.html')
    
def inicialaluno(request):
    if request.user.is_authenticated:

        projeto = projetos.objects.filter(aluno=request.user)
        atividade = atividades.objects.filter(aluno=request.user)
        return render(request, 'inicial-aluno.html', {'projeto': projeto, 'atividade': atividade})
    
    return redirect('login')    

@has_role_decorator('professor')
def inicialprofessor(request):
    if request.user.is_authenticated:

        projeto = projetos.objects.filter(orientador=request.user)
        return render (request, 'inicial-professor.html', {'projeto': projeto})
    return redirect('login')

def projeto_view(request, id):
    if request.user.is_authenticated:
        projeto = projetos.objects.filter(id=id)
        atividade = atividades.objects.filter(projeto=id)

        return render (request, 'InformacoesProjeto.html', {'projeto': projeto, 'atividade': atividade})
    
    return redirect('login')

@has_role_decorator('professor')
def cadastrar_projeto(request):
    if request.user.is_authenticated:
        
        form = ProjetoForm(request.POST or None)

        if form.is_valid():
            form.instance.orientador = request.user
            form.save()
            return redirect ('index')

        return render(request, 'CadastroProjeto.html', {'form': form})
   
    return redirect('login')

@has_role_decorator('professor')
def cadastrar_atividade(request):
    if request.user.is_authenticated:

        form = AtividadeForm(request.POST or None)

        if form.is_valid():
            form.instance.orientador = request.user
            form.save()
            return redirect ('index')
        
        return render (request, 'CadastroAtividade.html', {'form': form})
    return redirect('login')

@has_role_decorator('professor')
def excluir_projeto(request, id):
    if request.user.is_authenticated:
        projeto = projetos.objects.get(id=id)

        if request.method == 'POST':
            projeto.delete()
            return redirect('inicialprofessor')
        
        return render (request, 'delete-projeto.html', {'projeto':projeto})
    return redirect('login')

def excluir_atividade(request, id):
    if request.user.is_authenticated:
        atividade = atividades.objects.get(id=id)

        if request.method == 'POST':
            atividade.delete()
            return redirect('inicialprofessor')
        
        return render (request, 'delete-atividade.html', {'atividade':atividade})
    return redirect('login')

@has_role_decorator('professor')
def editar_projeto(request, id):
    if request.user.is_authenticated:
        projeto = projetos.objects.get(id=id)
        form = ProjetoForm(request.POST or None, instance = projeto)

        if form.is_valid():
            form.save()
            return redirect('inicialprofessor')
        return render(request, 'editar-projeto.html', {'form':form, 'projeto': projeto})
    return redirect('login')

def editar_atividade(request, id):
    if request.user.is_authenticated:
        atividade = atividades.objects.get(id=id)
        form = AtividadeForm(request.POST or None, instance = atividade)

        if form.is_valid():
            form.save()
            return redirect ('inicialprofessor')
        return render(request, 'editar-atividade.html', {'form':form, 'atividade': atividade})
    return redirect('login')

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username = username).first()
        if user:
            return HttpResponse('esse nome de usuario ja esta em uso')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        assign_role(user, 'aluno')
        user.save()
        return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('login')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user) 
            return redirect('index')
        else:
            return HttpResponse('email ou senha invalidos')
