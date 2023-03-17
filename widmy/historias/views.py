from django.shortcuts import render
from .logic import historias_logic as hl
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def historias_view(request):
    if request.method == 'GET':
        documento = request.GET.get("documento", None)
        if documento:
            historia = hl.get_historia(documento)
            historia_dto = serializers.serialize('json', [historia,])
            return HttpResponse(historia_dto, 'application/json')
        else:
            historias = hl.get_historias()
            historias_dto = serializers.serialize('json', historias)
            return HttpResponse(historias_dto, 'application/json')
    
    if request.method == 'POST':
        historia = hl.create_historia(request)
        historia_dto = serializers.serialize('json', [historia])
        return HttpResponse(historia_dto, 'application/json')
    
@csrf_exempt
def historia_view(request, documento):
    if request.method == 'GET':
        historia = hl.get_historia(documento)
        historia_dto = serializers.serialize('json', [historia])
        return HttpResponse(historia_dto, 'application/json')
    
    if request.method == 'PUT':
        historia = hl.update_historia(documento, request)
        historia_dto = serializers.serialize('json', [historia])
        return HttpResponse(historia_dto, 'application/json')