from django.contrib import admin
from .models import Pagina,Contato
admin.site.register(Pagina)


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'criado_em')
    search_fields = ('nome', 'email')
    readonly_fields = ('nome', 'email', 'mensagem', 'criado_em') # Apenas leitura
