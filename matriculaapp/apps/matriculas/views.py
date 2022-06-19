from django.shortcuts import render, get_object_or_404, redirect
from .forms import MatriculaForm, MatriculaItemForm
from .models import Matricula , MatriculaItem, Disciplina, Aluno

# Create your views here.

def add_matricula(request, id_aluno):
    template_name = 'matriculas/add_matricula.html'
    context = {}
    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.aluno = Aluno.objects.get(id=id_aluno)
            f.user = request.user
            f.save()
            form.save_m2m()
            return redirect('matriculas:list_matriculas')
    form = MatriculaForm()
    context['form'] = form
    return render(request, template_name, context)

def list_matriculas(request):
    template_name = 'matriculas/list_matriculas.html'
    matriculas = Matricula.objects.filter(user=request.user)
    matricula_items = MatriculaItem.objects.filter()
    disciplinas = Disciplina.objects.filter(user=request.user)
    alunos = Aluno.objects.filter(user=request.user)
    context = {
        'matriculas': matriculas,
        'matricula_items': matricula_items,
        'disciplinas': disciplinas,
        'alunos': alunos
    }
    return render(request, template_name, context)

def delete_matricula(request, id_matricula):
    matricula = Matricula.objects.get(id=id_matricula)
    matricula.delete()
    return redirect('matriculas:list_matriculas')

def add_matricula_item(request, id_matricula):
    template_name = 'matriculas/add_matricula_item.html'
    context = {}
    if request.method == 'POST':
        form = MatriculaItemForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.matricula = Matricula.objects.get(id=id_matricula)
            f.user = request.user            
            f.save()
            form.save_m2m()
            return redirect('matriculas:list_matriculas')
    form = MatriculaItemForm()
    context['form'] = form
    return render(request, template_name, context)

def delete_matricula_item(request, id_matricula_item):
    matriculaitem = MatriculaItem.objects.get(id=id_matricula_item)
    matriculaitem.delete()
    return redirect('matriculas:list_matriculas')

def edit_matricula_status(request, id_matricula):
    template_name = 'matriculas/edit_matricula_status.html'
    context ={}
    matricula = get_object_or_404(Matricula, id=id_matricula, user=request.user)
    if request.method == 'POST':
        form = MatriculaForm(request.POST, instance=matricula)
        if form.is_valid():
            form.save()
            return redirect('matriculas:list_matriculas')
    form = MatriculaForm(instance=matricula)
    context['form'] = form
    return render(request, template_name, context)
