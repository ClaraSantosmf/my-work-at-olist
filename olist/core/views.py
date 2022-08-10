import json
from django.http import JsonResponse

from olist.core.models import Autor


def autores(request):
    #response = HttpResponse('ok', content_type="text/plain")

    response = [autor.to_dict() for autor in Autor.objects.all()]

    return JsonResponse({'dados': autores})
