from django.shortcuts import render, redirect
from django.db import models
from TestApp.forms import EventoForm, InicioPageForm, ContactoPageForm, PresentacionForm
from TestApp.models import Evento, InicioPage, ContactoPage, PresentacionRegistro


def home(request):
    current_events = Evento.objects.filter(active = 1)
    if current_events.count() == 1:
        home = current_events[0].inicio
        return render(request, 'TestApp/home.html', {'home' : home})

    return render(request, 'TestApp/home.html')

def programa(request):
    current_events = Evento.objects.filter(active = 1)
    if current_events.count() == 1:
        programa = current_events[0].programa
        return render(request, 'TestApp/programa.html', {'programa' : programa})

    return render(request, 'TestApp/programa.html')

def poster(request):
    current_events = Evento.objects.filter(active = 1)
    if current_events.count() == 1:
        poster = current_events[0].poster
        return render(request, 'TestApp/poster.html', {'poster' : poster})

    return render(request, 'TestApp/poster.html')

def ubicacion(request):
    current_events = Evento.objects.filter(active = 1)
    if current_events.count() == 1:
        ubicacion = current_events[0].ubicacion
        return render(request, 'TestApp/ubicacion.html', {'ubicacion' : ubicacion})

    return render(request, 'TestApp/ubicacion.html')

def contacto(request):
    current_events = Evento.objects.filter(active = 1)
    if current_events.count() == 1:
        contacto = current_events[0].contacto
        return render(request, 'TestApp/contacto.html', {'contacto' : contacto})

    return render(request, 'TestApp/contacto.html')

def ponencias(request):
        form = PresentacionForm()
        return render(request, 'TestApp/ponencias.html', {'form': form})

def ediciones(request):
    current_events = Evento.objects.filter(active = 1)
    if current_events.count() == 1:
        edicion = current_events[0].edicion
        return render(request, 'TestApp/ediciones.html', {'' : edicion})

    return render(request, 'TestApp/ediciones.html')

# Vistas de administrador
def evento(request):
    return render(request, 'TestApp/evento.html')

def login(request):
    return render(request, 'TestApp/AdminFront/login.html')

def iterAdmin(request):
    eventos = Evento.objects.all()
    
    if Evento.objects.count() > 0:
    	return render(request, 'TestApp/AdminFront/edicionesFront.html', {'iteracion' : eventos[0], 'iteracion_list' : eventos})
    	
    return render(request, 'TestApp/AdminFront/edicionesFront.html')

def informe(request):
    return render(request, 'TestApp/AdminFront/informe.html')

def inicioAdmin(request):
    form = InicioPageForm()
    return render(request, 'TestApp/AdminFront/inicioAdmin.html', {'form': form})

def contactoAdmin(request):
    form = ContactoPageForm()
    return render(request, 'TestApp/AdminFront/contactoAdmin.html', {'form': form})

# Controladores
def savemail(request):  
    if request.method == "POST":  
        form = EventoForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EventoForm()  
    return render(request,'index.html',{'form':form})  

def remove_iteration(request):
    event_name = request.POST.get("nombre_evento") #Desde el view, la seleccion de evento a borrar tiene que venir con ese nombre 
                                                    #y que corresponda con el nombre en la db.
    try:  
        event = Evento.objects.get(nombre_evento = event_name)

        event.inicio.delete()
        event.programa.delete()
        event.poster.delete()
        event.ubicaciones.delete()
        event.contacto.delete()
        event.registro.delete()
        event.anteriores.delete()
        event.base.delete()

        event.delete()

    except Evento.DoesNotExist:
        print("Evento no existe")

    return render(request, 'TestApp/home.html') #esto es solo mientras se construye la pagina en donde el administrador podra eliminar ediciones del evento




