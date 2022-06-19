from django.shortcuts import render, get_object_or_404, redirect
from .forms import CursoForm
from .models import Curso
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/contas/login/')
def add_curso(request):
    template_name = 'cursos/add_curso.html'
    context = {}
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('cursos:list_cursos')
    form = CursoForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_cursos(request):
    template_name = 'cursos/list_cursos.html'
    cursos = Curso.objects.filter()
    context = {
        'cursos': cursos
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_curso(request, id_curso):
    template_name = 'cursos/add_curso.html'
    context ={}
    curso = get_object_or_404(Curso, id=id_curso)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos:list_cursos')
    form = CursoForm(instance=curso)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_curso(request, id_curso):
    curso = Curso.objects.get(id=id_curso)
    curso.delete()
    return redirect('cursos:list_cursos')