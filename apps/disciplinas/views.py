from django.shortcuts import render, get_object_or_404, redirect
from .forms import DisciplinaForm
from .models import Disciplina, Areadeconhecimento, DisciplinaAreadeconhecimento
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/contas/login/')
def add_disciplina(request):
    template_name = 'disciplinas/add_disciplina.html'
    context = {}
    if request.method == 'POST':
        form = DisciplinaForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            form.save_m2m()
            return redirect('disciplinas:list_disciplinas')
    form = DisciplinaForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_disciplinas(request):
    template_name = 'disciplinas/list_disciplinas.html'
    disciplina_areadeconhecimento = DisciplinaAreadeconhecimento.objects.filter()
    areadeconhecimento = Areadeconhecimento.objects.filter(user=request.user)
    disciplinas = Disciplina.objects.filter(user=request.user)
    context = {
        'disciplinas': disciplinas,
        'areadeconhecimento': areadeconhecimento,
        'disciplina_areadeconhecimento': disciplina_areadeconhecimento,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_disciplina(request, id_disciplina):
    template_name = 'disciplinas/add_disciplina.html'
    context ={}
    disciplina = get_object_or_404(Disciplina, id=id_disciplina, user=request.user)
    if request.method == 'POST':
        form = DisciplinaForm(request.POST, request.FILES,  instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('disciplinas:list_disciplinas')
    form = DisciplinaForm(instance=disciplina)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_disciplina(request, id_disciplina):
    disciplina = Disciplina.objects.get(id=id_disciplina)
    if disciplina.user == request.user:
        disciplina.delete()
    else:
        return redirect('core:home')
    return redirect('disciplinas:list_disciplinas')