from rest_framework.viewsets import ModelViewSet

from livraria.models import Autor
from livraria.serializers.autor import AutorSerializer


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
