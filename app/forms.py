from django import forms
from .models import Contato

# Mixin para adicionar classes Bootstrap padrão
class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            # Adiciona a classe form-control e espaçamento inferior
            self.fields[field].widget.attrs.update({'class': 'form-control mb-2'})

class ContatoForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite seu nome'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Digite seu e-mail'}),
            'mensagem': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Digite sua mensagem'}),
        }
