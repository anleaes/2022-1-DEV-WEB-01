from django.shortcuts import render, get_object_or_404, redirect
from .forms import AreadeconhecimentoForm
from .models import Areadeconhecimento

# Create your views here.

def add_areadeconhecimento(request):
    template_name = 'areadeconhecimento/add_areadeconhecimento.html'
    context = {}
    if request.method == 'POST':
        form = AreadeconhecimentoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            form.save_m2m()
            return redirect('areadeconhecimento:list_areadeconhecimento')
    form = AreadeconhecimentoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_areadeconhecimento(request):
    template_name = 'areadeconhecimento/list_areadeconhecimento.html'
    areadeconhecimento = Areadeconhecimento.objects.filter(user=request.user)
    context = {
        'areadeconhecimento': areadeconhecimento
    }
    return render(request, template_name, context)

def edit_areadeconhecimento(request, id_areadeconhecimento):
    template_name = 'areadeconhecimento/add_areadeconhecimento.html'
    context ={}
    areadeconhecimento = get_object_or_404(Areadeconhecimento, id=id_areadeconhecimento, user=request.user)
    if request.method == 'POST':
        form = AreadeconhecimentoForm(request.POST, instance=areadeconhecimento)
        if form.is_valid():
            form.save()
            return redirect('areadeconhecimento:list_areadeconhecimento')
    form = AreadeconhecimentoForm(instance=areadeconhecimento)
    context['form'] = form
    return render(request, template_name, context)

def delete_areadeconhecimento(request, id_areadeconhecimento):
    areadeconhecimento = Areadeconhecimento.objects.get(id=id_areadeconhecimento)
    if areadeconhecimento.user == request.user:
        areadeconhecimento.delete()
    else:
        return redirect('core:home')
    return redirect('areadeconhecimento:list_areadeconhecimento')
