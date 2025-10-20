import json
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Categoria
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

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