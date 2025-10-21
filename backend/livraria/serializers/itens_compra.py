from rest_framework.serializers import ModelSerializer, SerializerMethodField
from livraria.serializers.livro import LivrosDetailSerializer
from livraria.models import ItensCompra

class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()
    livro = LivrosDetailSerializer()

    def get_total(self, instance):
        return instance.quantidade * instance.livro.preco
    
    class Meta:
        model = ItensCompra
        fields = ('livro', 'quantidade', 'total', )
        depth = 2