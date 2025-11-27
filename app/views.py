from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .models import Pagina
from .forms import ContatoForm, CadastroForm

def home(request):
    pagina = Pagina.objects.first()
    
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('home')
    else:
        form = ContatoForm()

    context = {'pagina': pagina, 'form_contato': form}
    return render(request, 'home.html', context)

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CadastroForm()
    return render(request, 'cadastro.html', {'form': form})

