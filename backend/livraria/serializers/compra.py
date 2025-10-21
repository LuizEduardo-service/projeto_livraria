from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
from livraria.serializers.itens_compra import ItensCompraSerializer
from livraria.models import Compra

class CompraSerializer(ModelSerializer):
    status = SerializerMethodField()
    usuario = CharField(source='usuario.email')
    itens = ItensCompraSerializer(many=True)

    def get_status(self, instance):
        return instance.get_status_display()
    class Meta:
        model = Compra
        exclude = ('updated_at', 'created_at', )