from django.contrib import admin

from .models import Autor, Categoria, Editora

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Autor)
