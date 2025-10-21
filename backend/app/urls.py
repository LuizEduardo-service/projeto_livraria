
from django.contrib import admin
from django.urls import path, include

from livraria.views.categoria import CategoriaViewSet
from livraria.views.editora import EditoraViewSet
from livraria.views.livro import LivrosViewSet

from rest_framework import routers

routes = routers.DefaultRouter()
routes.register(r'categorias', CategoriaViewSet)
routes.register(r'editoras', EditoraViewSet)
routes.register(r'livros', LivrosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(routes.urls))
]
