from django.shortcuts import render
from .logic import adendas_logic as al
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def adendas_view(request):
    if request.method == 'GET':
        identificador = request.GET.get("identificador", None)
        if identificador:
            adenda = al.get_adenda(identificador)
            adenda_dto = serializers.serialize('json', [adenda,])
            return HttpResponse(adenda_dto, 'application/json')
        else:
            adendas = al.get_adendas()
            adendas_dto = serializers.serialize('json', adendas)
            return HttpResponse(adendas_dto, 'application/json')
        
    if request.method == 'POST':
        adenda = al.create_adenda(request)
        adenda_dto = serializers.serialize('json', [adenda])
        return HttpResponse(adenda_dto, 'application/json')
    
@csrf_exempt
def adenda_view(request, identificador):
    if request.method == 'GET':
        adenda = al.get_adenda(identificador)
        adenda_dto = serializers.serialize('json', [adenda])
        return HttpResponse(adenda_dto, 'application/json')
    
    if request.method == 'PUT':
        adenda = al.update_adenda(identificador, request)
        adenda_dto = serializers.serialize('json', [adenda])
        return HttpResponse(adenda_dto, 'application/json')
