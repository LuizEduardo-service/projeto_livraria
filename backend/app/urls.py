
from django.contrib import admin
from django.urls import path

from livraria import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categorias/', view=views.CategoriaView.as_view(), name='categorias'),
    path('categorias-apiview/', view=views.CategoriaList.as_view(), name='categorias-api')
]
