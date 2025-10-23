from rest_framework.viewsets import ModelViewSet
from livraria.models import Compra
from livraria.serializers.compra import CompraSerializer, CriarEditarCompraSerializer

class CompraViewSet(ModelViewSet):

    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CompraSerializer
        return CriarEditarCompraSerializer
    