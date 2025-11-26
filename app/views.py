from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Pagina
from .forms import ContatoForm

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
