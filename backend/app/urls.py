
from django.contrib import admin
from django.urls import path, include

from livraria.views.categoria import CategoriaViewSet
from livraria.views.editora import EditoraViewSet
from livraria.views.livro import LivrosViewSet
from livraria.views.autor import AutorViewSet
from livraria.views.compra import CompraViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import routers

routes = routers.DefaultRouter()
routes.register(r'categorias', CategoriaViewSet)
routes.register(r'editoras', EditoraViewSet)
routes.register(r'livros', LivrosViewSet)
routes.register(r'autores', AutorViewSet)
routes.register(r'compras', CompraViewSet)


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include(routes.urls)), 
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
