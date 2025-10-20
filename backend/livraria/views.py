import json
from django.http import HttpResponse
from django.views import View
from .models import Categoria

# Create your views here.
class CategoriaView(View):

    def get(self, request):
        data = list(Categoria.objects.all())
        formatted_data = json.dumps(data, ensure_ascii=False)
        return HttpResponse(formatted_data, content_type='application/json')
