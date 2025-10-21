
from django.contrib import admin
from django.urls import path, include

from livraria.views.categoria import CategoriaViewSet

from rest_framework import routers

routes = routers.DefaultRouter()
routes.register(r'categorias', CategoriaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(routes.urls))
]
