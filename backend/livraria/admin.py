from django.contrib import admin

from .models import Autor, Categoria, Compra, Editora, ItensCompra, Livros

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livros)
admin.site.register(Compra)
admin.site.register(ItensCompra)
