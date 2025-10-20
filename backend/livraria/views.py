import json
from typing import List

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Categoria


@method_decorator(csrf_exempt, name='dispatch')
class CategoriaView(View):

    def get(self, request):
        data = list(Categoria.objects.values())
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

    def post(self, request):
        json_data = json.loads(request.body)
        nova_categoria: Categoria = Categoria.objects.create(**json_data)
        data = {"id": nova_categoria.id, 'descricao': nova_categoria.descricao}
        return JsonResponse(data=data)


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'descricao', )


class CategoriaList(APIView):

    def get(self, request):
        categorias: List[Categoria] = Categoria.objects.all()
        serializers = CategoriaSerializer(categorias, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
