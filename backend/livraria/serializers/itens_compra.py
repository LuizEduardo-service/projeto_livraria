from rest_framework.serializers import ModelSerializer, SerializerMethodField

from livraria.models import ItensCompra
from livraria.serializers.livro import LivrosDetailSerializer


class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()
    livro = LivrosDetailSerializer()

    def get_total(self, instance):
        return instance.quantidade * instance.livro.preco

    class Meta:
        model = ItensCompra
        fields = ('livro', 'quantidade', 'total', )
        depth = 2
