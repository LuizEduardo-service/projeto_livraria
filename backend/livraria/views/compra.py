import time
from rest_framework.viewsets import ModelViewSet
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from livraria.models import Compra
from livraria.serializers.compra import (
    CompraSerializer,
    CriarEditarCompraSerializer,
)


class CompraViewSet(ModelViewSet):

    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CompraSerializer
        return CriarEditarCompraSerializer
    
    def get_queryset(self):
        print("buscando da base de dados!")
        time.sleep(2)
        return super().get_queryset()

    @method_decorator(cache_page(60 * 2, key_prefix='compra_list'))
    def list(self, request, *args, **kwargs):
        print("buscando do cache-redis!")
        return super().list(request, *args, **kwargs)
