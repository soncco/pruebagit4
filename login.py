from django.models import Model

class Usuario(Model.models):
    nombre = models.Charfield(max_length=155)
