from django.db import models
from django.contrib.auth.models import User

class Referencias(models.Model):
    arquivo = models.FileField(upload_to='referencias')

    def __str__(self):
        return self.arquivo.url

class Jobs(models.Model):
    categoria_choice = (
        ('D', 'Design'),
        ('EV', 'Edição de Vídeo')
    )

    status_choice = (
        ('C', 'Em criaçao'),
        ('AA', 'Arguardando aprovação'),
        ('F', 'Finalizado')
    )

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    categoria = models.CharField(max_length=2, choices=categoria_choice, default='D')
    prazo_entrega = models.DateTimeField()
    preco = models.FloatField()
    Referencias = models.ManyToManyField(Referencias)
    profissional = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    reservado = models.BooleanField(default=False)
    status = models.CharField(max_length=2, choices=status_choice, default='C')
    arquivo_final = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.titulo