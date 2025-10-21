from livraria.models import Categoria
from rest_framework.viewsets import ModelViewSet

from livraria.serializers.categoria import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer