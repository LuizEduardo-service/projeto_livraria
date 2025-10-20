from django.contrib import admin

from .models import Autor, Categoria, Compra, Editora, ItensCompra, Livros

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livros)

class ItensInline(admin.TabularInline):
    model = ItensCompra

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = (ItensInline, )
