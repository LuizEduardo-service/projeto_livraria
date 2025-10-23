from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField, HiddenField, CurrentUserDefault
from livraria.serializers.itens_compra import ItensCompraSerializer
from livraria.models import Compra, ItensCompra

class CompraSerializer(ModelSerializer):
    status = SerializerMethodField()
    usuario = CharField(source='usuario.email')
    itens = ItensCompraSerializer(many=True)

    def get_status(self, instance):
        return instance.get_status_display()
    class Meta:
        model = Compra
        fields = ('id', "status", 'usuario', 'itens', 'total',)

class CriarEditarItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ('livro', 'quantidade')


class CriarEditarCompraSerializer(ModelSerializer):
    itens = CriarEditarItensCompraSerializer(many=True)
    usuario = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Compra
        fields = ('usuario', 'itens')

    def create(self, validated_data):
        itens = validated_data.pop('itens')
        compra = Compra.objects.create(**validated_data)
        for item in itens:
            ItensCompra.objects.create(compra=compra, **item)
        compra.save()
        return compra
    
    def update(self, instance, validated_data):
        itens = validated_data.pop('itens')

        if itens:
            instance.itens.all().delete()
            for item in itens:
                ItensCompra.objects.create(compra=instance, **item)
            instance.save()
            return instance