from rest_framework.serializers import ModelSerializer

from livraria.models import Autor


class AutorSerializer(ModelSerializer):

    class Meta:
        model = Autor
        exclude = ('updated_at', 'created_at', )
