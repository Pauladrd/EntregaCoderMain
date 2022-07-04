from pyexpat import model
from django import forms
from .models import ModeloCliente
from .models import ModeloTramite
from .models import ModeloFecha
from .models import ModeloDocumentacion
from .models import ModeloPago

class FormularioCliente(forms.ModelForm):
    class Meta: 
        model = ModeloCliente
        fields = ['nombre', 'apellido', 'email']
        widgets = { 
            'nombre': forms.TextInput(attrs={'class': 'form-control col-md-8'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control col-md-8'}),
            'email': forms.EmailInput(attrs={'class': 'form-control col-md-8'}),
        }

class FormularioVerCliente(forms.ModelForm):
    class Meta:
        model = ModeloCliente
        fields = ['nombre', 'apellido', 'email', 'documentos']
        widgets = { 
            'nombre': forms.TextInput(attrs={'class': 'form-control col-md-8'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control col-md-8'}),
            'email': forms.EmailInput(attrs={'class': 'form-control col-md-8'}),
            'documentos': forms.CheckboxInput(attrs={'class': 'form-control'})
        }

class FormularioTramite(forms.ModelForm):
    class Meta: 
        model = ModeloTramite
        fields = '__all__'
        widgets = { 
            'type': forms.Select(attrs={'class': 'form-control col-md-8'}),
        }

class FormularioFecha(forms.ModelForm):
    class Meta: 
        model = ModeloFecha
        fields = '__all__'
        widgets = { 
            'dia': forms.TextInput(attrs={'class': 'form-control col-md-8'}),
            'mes': forms.TextInput(attrs={'class': 'form-control col-md-8'}),
            'año': forms.TextInput(attrs={'class': 'form-control col-md-8'}),
        }

class FormularioDocumentacion(forms.ModelForm):
    class Meta: 
        model = ModeloDocumentacion
        fields = '__all__'
        widgets = { 
            'documento': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
        }


class FormularioPago(forms.ModelForm):
    class Meta: 
        model = ModeloPago
        fields = '__all__'
        widgets = { 
            'nombre': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
        }

# class FormularioLogin(forms.ModelForm):
#     class Meta: 
#         model = 
#         fields = '__all__'
#         widgets = { 
#             'nombre': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
#         }