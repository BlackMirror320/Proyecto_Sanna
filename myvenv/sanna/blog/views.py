from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect, render
from django.views.generic.edit import FormView

#Importado de modelos que aún no existen, solo son un ejemplo.
#from blog.forms import CreateUserForm, ClienteForm, ProductForm
from blog.models import *
from django import forms

#Imports para el manejo de usuarios
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.
# <----- REDIRECCIONES POR CARPETA ----->
# <----- PRINCIPAL ----->
def index(request):
    return render(request, 'Principal/inicio.html', {'title':'index'})

def inicio(request):
    return render(request, 'Principal/inicio.html', {'title':'inicio'})

def contacto(request):
    return render(request, 'Principal/contacto.html', {'title':'contacto'})

#ESTE ES UN EXPERIMENTAL PARA VER SI SIENDO SUPER USER LOGEADO, LLEVABA COMO INDEX AL INICIO_FARMACIA 
#@login_required(login_url='login')                              #Solo se muestra logeado
#@user_passes_test((lambda u: u.is_superuser),login_url='login') #Indico Superusuario
#def index(request):
#    return render(request, 'Principal/inicio_farmacia.html', {'title':'index'})

@login_required(login_url='login')                              #Solo se muestra logeado
@user_passes_test((lambda u: u.is_superuser),login_url='login') #Indico Superusuario
def inicio_farmacia(request):
    return render(request, 'Principal/inicio_farmacia.html', {'title':'index'})

# <=============================================>


# <----- CREDENCIALES ----->
#def registro(request):
#    if request.user.is.authenticated:
#        return redirect('/Principal/inicio.html')
#    else:
#        form = CreateUserForm() #Hay que crear el form de esto
#        if request.method == 'POST':
#            form = CreateUserForm(request.POST)
#            if form.is_valid():
#                form.save()
#                user = form.cleaned_data.get('username')
#                messages.success(request, 'Se registró el usuario ' + user)
#                return redirect('Credenciales/login.html')
#        return render(request, 'Credenciales/registro.html', {'form':form})

#def login(request):
#    if request.user.is_authenticated:
#        return redirect('/Principal/inicio.html')
#    else:
#        if request.method == 'POST':
#            username = request.POST.get('username')
#            password = request.POST.get('password')
#
#            user = authenticate(request, username = username, password=password)
#
#            if user is not None:
#                login(request,user)
#                return redirect('/Principal/inicio.html')
#            else:
#                messages.info(request,'Usuario o password incorrecto')
#        return render(request,'Credenciales/login.html')
#    
#def logoutUser(request):
#    logout(request)
#    return redirect('Credenciales/login.html')

# <=============================================>


# <----- LISTAMEDICAMENTOS ----->


# <=============================================>


# <----- PERFILES ----->


# <=============================================>


# <----- RESET_PASSWORD ----->


# <=============================================>