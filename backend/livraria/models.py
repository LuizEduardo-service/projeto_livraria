from django.contrib.auth.models import User
from django.db import models
from django.db.models import F

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Categoria(BaseModel):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao


class Editora(BaseModel):
    nome = models.CharField(max_length=255)
    site = models.URLField()

    def __str__(self):
        return self.nome


class Autor(BaseModel):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'


class Livros(BaseModel):
    titulo = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=32)
    quantidade = models.IntegerField()
    preco = models.FloatField(default=0.0)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='livros')
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name='livros')
    autores = models.ManyToManyField(Autor, related_name='livros')

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'


class Compra(BaseModel):

    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, 'Carrinho'
        REALIZADO = 2, 'Realizado'
        PAGO = 3, 'Pago'
        ENTREGUE = 4, 'Entregue'

    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='compras')
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'

    @property
    def total(self):
        queryset = self.itens.all().aggregate(total=models.Sum(F('quantidade') * F('livro__preco')))
        return queryset['total']

class ItensCompra(BaseModel):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='itens')
    livro = models.ForeignKey(Livros, on_delete=models.PROTECT, related_name='+')
    quantidade = models.IntegerField()
