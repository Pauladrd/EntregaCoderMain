from django.contrib import admin
from .models import ModeloCliente, ModeloDocumentacion, ModeloFecha, ModeloPago, ModeloTramite


# Register your models here.
admin.site.register(ModeloCliente)
admin.site.register(ModeloDocumentacion)
admin.site.register(ModeloFecha)
admin.site.register(ModeloPago)
admin.site.register(ModeloTramite)
