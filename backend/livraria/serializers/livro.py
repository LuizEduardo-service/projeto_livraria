from rest_framework.serializers import ModelSerializer

from livraria.models import Livros


class LivrosSerializer(ModelSerializer):
    
    class Meta:
        model = Livros
        fields = '__all__'



class LivrosDetailSerializer(ModelSerializer):

    class Meta:
        model = Livros
        fields = '__all__'
        depth = 1