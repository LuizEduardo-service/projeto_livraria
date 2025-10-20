from django.db import models

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
