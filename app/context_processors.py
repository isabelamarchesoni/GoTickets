from .models import Pagina

def dados_pagina(request):
    try:
        # Tenta pegar a primeira (e única) instância de Pagina
        pagina_obj = Pagina.objects.first() 
    except:
        pagina_obj = None

    return {
        'pagina': pagina_obj
    }