from django.contrib import admin
from .models import Pagina, Produto, Contato, Pedido
admin.site.register(Pagina)

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'criado_em')
    search_fields = ('nome', 'email')
    readonly_fields = ('nome', 'email', 'mensagem', 'criado_em') 

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'atualizado_em')
    search_fields = ('nome', 'descricao')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'produto', 'quantidade', 'total', 'data')
    list_filter = ('data',)
