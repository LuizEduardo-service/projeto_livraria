from rest_framework.serializers import ModelSerializer
from livraria.models import Compra

class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        exclude = ('updated_at', 'created_at', )