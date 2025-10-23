from rest_framework.viewsets import ModelViewSet

from livraria.models import Livros
from livraria.serializers.livro import LivrosDetailSerializer, LivrosSerializer


class LivrosViewSet(ModelViewSet):
    queryset = Livros.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LivrosDetailSerializer
        return LivrosSerializer
