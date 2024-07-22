from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Persona
from .forms import PersonaForm

def index(request):
    return render(request,'index.html')
def persona_list(request):
    personas = Persona.objects.all()
    return render(request, 'persona_list.html', {'personas': personas})

def persona_create(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('persona_list'))
    else:
        form = PersonaForm()
    return render(request, 'persona_form.html', {'form': form})

def persona_update(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect(reverse('persona_list'))
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'persona_form.html', {'form': form})

def persona_delete(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == 'POST':
        persona.delete()
        return redirect(reverse('persona_list'))
    return render(request, 'persona_confirm_delete.html', {'persona': persona})