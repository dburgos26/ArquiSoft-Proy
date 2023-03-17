from ..models import Historia

def get_historias():
    historias = Historia.objects.all()
    return historias

def get_historia(documento):
    historia = Historia.objects.get(documento=documento)
    return historia

def update_historia(documento, new_historia):
    historia = get_historia(documento)
    historia.documento = new_historia["documento"]
    historia.nombre = new_historia["nombre"]
    historia.apellido = new_historia["apellido"]
    historia.fecha_nacimiento = new_historia["fecha_nacimiento"]
    historia.sexo = new_historia["sexo"]
    historia.save()
    return historia

def create_historia(historia):
    historia = Historia(documento=historia["documento"], nombre=historia["nombre"], apellido=historia["apellido"], fecha_nacimiento=historia["fecha_nacimiento"], sexo=historia["sexo"])
    historia.save()
    return historia
