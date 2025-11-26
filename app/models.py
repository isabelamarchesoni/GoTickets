from django.db import models

class Pagina(models.Model):
    nome_do_site = models.CharField(max_length=100)
    logo_do_site = models.ImageField(upload_to='site/', blank=True, null=True)
    texto_chamada = models.CharField(max_length=200, help_text="Texto principal do banner")
    texto_sobre = models.TextField()
    imagem_sobre = models.ImageField(upload_to='site/', blank=True, null=True)
    endereco = models.CharField(max_length=255)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_do_site

    class Meta:
        verbose_name = "Configuração da Página"
        verbose_name_plural = "Configurações da Página"
        
class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensagem de {self.nome}"
