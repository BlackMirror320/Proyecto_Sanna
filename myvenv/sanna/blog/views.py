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
def inicio(request):
    return render(request, 'Principal/inicio.html', {'title':'index'})

# <=============================================>


# <----- CREDENCIALES ----->


# <=============================================>


# <----- LISTAMEDICAMENTOS ----->


# <=============================================>


# <----- PERFILES ----->


# <=============================================>


# <----- RESET_PASSWORD ----->


# <=============================================>