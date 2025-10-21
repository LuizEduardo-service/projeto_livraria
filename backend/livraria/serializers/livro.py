from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from livraria.serializers.editora import EditoraSerializer
from livraria.models import Autor, Livros


class LivrosSerializer(ModelSerializer):
    
    class Meta:
        model = Livros
        # fields = '__all__'
        exclude = ('updated_at', 'created_at', )



class LivrosDetailSerializer(ModelSerializer):
    categoria = CharField(source='categoria.descricao')
    editora = EditoraSerializer()
    autores = SerializerMethodField() # precisa cria o metodo get_autores
    class Meta:
        model = Livros
        # fields = '__all__'
        exclude = ('updated_at', 'created_at', )
        depth = 1

    def get_autores(self, intance):
        nome_autores: list = []
        autores = intance.autores.get_queryset()
        nome_autores = [autor.nome for autor in autores]
        return nome_autores