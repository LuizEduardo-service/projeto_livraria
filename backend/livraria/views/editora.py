from livraria.serializers.editora import EditoraSerializer
from livraria.models import Editora

from rest_framework.viewsets import ModelViewSet


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer