from ..models import Adenda

def get_adendas():
    adendas = Adenda.objects.all()
    return adendas

def get_adenda(identificador):
    adenda = Adenda.objects.get(identificador=identificador)
    return adenda

def update_adenda(identificador, new_adenda):
    adenda = get_adenda(identificador)
    adenda.identificador = new_adenda["identificador"]
    adenda.fecha = new_adenda["fecha"]
    adenda.descripcion = new_adenda["descripcion"]
    adenda.save()
    return adenda

def create_adenda(adenda):
    adenda = Adenda(identificador=adenda["identificador"], fecha=adenda["fecha"], descripcion=adenda["descripcion"])
    adenda.save()
    return adenda