from random import choices
from django.shortcuts import render, redirect
from django.template import loader
from .forms import FormularioCliente, FormularioTramite, FormularioFecha, FormularioDocumentacion, FormularioPago, FormularioVerCliente
from .models import ModeloCliente, ModeloDocumentacion, ModeloFecha, ModeloPago, ModeloTramite
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.db.models import Q

# Create your views here.

def clientes(request):
    miFormulario = FormularioCliente()
    misClientes = ModeloCliente.objects.all()

    if request.method == 'POST':
        miFormulario = FormularioCliente(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cliente = ModeloCliente(nombre = informacion['nombre'], apellido = informacion['apellido'], email = informacion['email'])
            cliente.save()
            return render(request, 'APPfinal/clientes.html', {'formulario':miFormulario, 'clientes':misClientes})
    else:
        return render(request, 'APPfinal/clientes.html', {'formulario':miFormulario, 'clientes':misClientes})

@login_required(login_url='login')
def verClienteView(request, pk):
    if request.method == 'POST':
        miFormulario = FormularioVerCliente(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cliente = ModeloCliente(id = pk, nombre = informacion['nombre'], apellido = informacion['apellido'], email = informacion['email'], documentos = informacion['documentos'])
            cliente.save()
            miFormulario = FormularioCliente()
            misClientes = ModeloCliente.objects.all()
            return render(request, 'APPfinal/clientes.html', {'formulario':miFormulario, 'clientes':misClientes})

    miFormulario = FormularioVerCliente()
    cliente = ModeloCliente.objects.get(id=pk)

    return render(request, 'APPfinal/ver-cliente.html', {'formulario':miFormulario, 'cliente': cliente})

def Tramite(request):
    data = {
            'form': ModeloTramite
    }
    miFormulario = FormularioTramite()
    misTramites = ModeloTramite.objects.all()

    if request.method == 'POST':
       
        miFormulario = FormularioTramite(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            tramite = ModeloTramite(tramite = informacion['tramite'])
            tramite.save()

            return render(request, 'APPfinal/Tramite.html', {'formulario':miFormulario, 'tramites': misTramites})

    
    else:
        return render(request, 'APPfinal/Tramite.html', {'formulario':miFormulario, 'tramites': misTramites})
    


def Fecha(request):
    miFormulario = FormularioFecha()
    misFechas = ModeloFecha.objects.all()

    if request.method == 'POST':
        miFormulario = FormularioFecha(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            fecha = ModeloFecha(dia = informacion['dia'], mes = informacion['mes'], año = informacion['año'])
            fecha.save()

            return render(request, 'APPfinal/fecha.html', {'formulario':miFormulario, 'fechas': misFechas})

    else:
        return render(request, 'APPfinal/fecha.html', {'formulario':miFormulario, 'fechas': misFechas})
    



def Documentacion(request):
    miFormulario = FormularioDocumentacion()
    misDocumentos = ModeloDocumentacion.objects.all()

    if request.method == 'POST':
        miFormulario = FormularioDocumentacion(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            documento = ModeloDocumentacion(documento = informacion['documento'], tipo = informacion['tipo'])
            documento.save()

            return render(request, 'APPfinal/documentacion.html', {'formulario':miFormulario, 'documentos': misDocumentos})

    else:
        return render(request, 'APPfinal/documentacion.html', {'formulario':miFormulario, 'documentos': misDocumentos})
    

def Pago(request):
    if request.method == 'POST':
        miFormulario = FormularioPago(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            pago = ModeloPago(mediodepago = informacion['mediodepago'], total = informacion['total'])
            pago.save()

            return render(request, 'APPfinal/pagos.html')

    else:
        miFormulario = FormularioPago()
        return render(request, 'APPfinal/pagos.html', {'formulario':miFormulario})
    


def index(self):
    index = loader.get_template('index.html')
    documento = index.render()


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('Nombre')
    else:
        form = AuthenticationForm()

    return render(request, 'APPfinal/login.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect('Nombre')

def sobremi(request):
    return render(request,'APPfinal/sobremi.html')

def buscarView(request):
    if request.method == 'GET':
        resultados = []
        busqueda = request.GET.get('buscar')
        srch = ModeloCliente.objects.filter(Q(nombre__icontains = busqueda) | Q(apellido__icontains = busqueda) | Q(email__icontains = busqueda))
        if srch is not None:
            resultados.append({'cliente': srch})
        srch = ModeloTramite.objects.filter(Q(tramite__icontains = busqueda))
        if srch is not None:
            resultados.append({'tramite': srch})
        srch = ModeloDocumentacion.objects.filter(Q(documento__icontains = busqueda) | Q(tipo__icontains = busqueda))
        if srch is not None:
            resultados.append({'documentacion': srch})
        return render(request, 'APPfinal/resultados.html', {'resultados': resultados})
    
    else:
        return render(request, 'APPfinal/resultados.html')
