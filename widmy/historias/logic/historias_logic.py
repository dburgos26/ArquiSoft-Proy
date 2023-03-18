import json
from ..models import Historia
from datetime import datetime

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

def create_historia(request):
    historia_json = json.loads(request.body)
    fecha_nacimiento_str = historia_json['fecha_nacimiento']
    historia = Historia(
        nombrePaciente=historia_json['nombre'],
        apellidoPaciente=historia_json['apellido'],
        edadPaciente=historia_json['edad'],
        documento=historia_json['documento'],
        fechaNacimiento=datetime.strptime(fecha_nacimiento_str, '%Y-%m-%d').date(),
        descripcion=historia_json['descripcion']
    )
    historia.save()
    return historia
