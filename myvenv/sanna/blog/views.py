from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect, render
from django.views.generic.edit import FormView

#Importado de modelos que aún no existen, solo son un ejemplo.
#from blog.forms import CreateUserForm, ClienteForm, ProductForm
#from blog.models import *
from django import forms

#Imports para el manejo de usuarios
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import *


# Create your views here.
# <----- REDIRECCIONES POR CARPETA ----->
# <----- PRINCIPAL ----->
def index(request):
    return render(request, 'Principal/inicio.html', {'title':'index'})

def inicio(request):
    return render(request, 'Principal/inicio.html', {'title':'inicio'})

def acercade(request):
    return render(request, 'Principal/acercade.html', {'title':'acercade'})



#ESTE ES UN EXPERIMENTAL PARA VER SI SIENDO SUPER USER LOGEADO, LLEVABA COMO INDEX AL INICIO_FARMACIA 
#@login_required(login_url='login')                              #Solo se muestra logeado
#@user_passes_test((lambda u: u.is_superuser),login_url='login') #Indico Superusuario
#def index(request):
#    return render(request, 'Principal/inicio_farmacia.html', {'title':'index'})

#@login_required(login_url='login')                              #Solo se muestra logeado
#@user_passes_test((lambda u: u.is_superuser),login_url='login') #Indico Superusuario
def inicio_farmacia(request):
    return render(request, 'Principal/inicio_farmacia.html', {'title':'index'})

# <=============================================>

# <----- LISTA DE MEDICAMENTOS ----->
def medicamentos(request):
    return render(request, 'ListaMedicamentos/medicamentos.html', {'title':'medicamentos'})

# <----- CREDENCIALES ----->
def registro(request):
    if request.user.is_authenticated:
        return redirect('index2')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Se registró el usuario ' + user)
                return redirect('login')
        return render(request, 'Credenciales/registro.html', {'form':form})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/Principal/inicio.html')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password=password)

            if user is not None:
                login(request,user)
                return redirect('inicio')
            else:
                messages.info(request,'Usuario o password incorrecto')
        return render(request,'Credenciales/loginPage.html')
    
def logoutUser(request):
    logout(request)
    return redirect('login')

# <=============================================>


# <----- ADMINMEDICAMENTOS ----->
@login_required(login_url='login')
@user_passes_test((lambda u: u.is_superuser),login_url='login')
def admin_medicamento(request):
    form = MedicamentoForm()
    medicamentos = Medicamento.objects.all()
    if request.method == 'POST':
        print(request.POST)
        form = MedicamentoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('admin_medicamento')
            except:
                pass
        else:
            form = MedicamentoForm
    context = {'form':form, 'medicamentos':medicamentos}
    return render(request, 'ListaMedicamentos/admin_medicamento.html', context)



@login_required(login_url='login')
@user_passes_test((lambda u: u.is_superuser),login_url='login')
def crea_medicamento(request):
    form = MedicamentoForm()
    medicamentos = Medicamento.objects.all()
    if request.method == 'POST':
        print(request.POST)
        form = MedicamentoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('admin_medicamento')
            except:
                pass
        else:
            form = MedicamentoForm
    context = {'form':form, 'medicamentos':medicamentos}
    return render(request, 'ListaMedicamentos/crea_medicamento.html', context)


@login_required(login_url='login')
@user_passes_test((lambda u: u.is_superuser),login_url='login')
def edita_medicamento(request, id):
    med = Medicamento.objects.get(id_medicamento=id)
    form = MedicamentoForm(instance=med)
    return render(request,'ListaMedicamentos/edita_medicamento.html', {'form':form, 'id_medicamento':med.id_medicamento})


@login_required(login_url='login')
@user_passes_test((lambda u: u.is_superuser),login_url='login')
def modificar(request,id):
    med = Medicamento.objects.get(id_medicamento=id)
    if request.method == 'POST':
        print(request.POST)
        form = MedicamentoForm(request.POST, request.FILES, instance=med)
        if form.is_valid():
            form.save()
            return redirect('admin_medicamento')
            #messages.success(request, "Cambios Realizados!")

@login_required(login_url='login')
@user_passes_test((lambda u: u.is_superuser),login_url='login')
def elimina_medicamento(request, id):
    med = Medicamento.objects.get(id_medicamento=id)
    med.delete()
    return redirect('admin_medicamento')

# <=============================================>


# <----- PERFILES ----->
@login_required(login_url='login')
def perfil_usuario(request):
    return render(request, 'Perfiles/perfil_usuario.html')

@login_required(login_url='login')
def perfil_admin(request,id):
    user = User.objects.get(id = id)
    form = CreateUserForm
    return render(request, 'Perfiles/perfil_admin.html', {'form':form, 'id':user.id})

@login_required(login_url='login')
def modificar_perfil(request,id):
    user = User.objects.get(id = id)
    if request.method == 'POST':
        print(request.POST)
        form = UserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('perfil_usuario')

# <=============================================>


# <----- RESET_PASSWORD ----->


# <=============================================>




# <----- Largo de la contraseña mínimo ----->
#class ValidatingPasswordChangeForm(auth.forms.PasswordChangeForm):
#    MIN_LENGTH = 8
#
#    def clean_new_password1(self):
#        password1 = self.cleaned_data.get('new_password1')
#
#        # At least MIN_LENGTH long
#        if len(password1) < self.MIN_LENGTH:
#            raise forms.ValidationError("The new password must be at least %d characters long." % self.MIN_LENGTH)
#
#        # At least one letter and one non-letter
#        first_isalpha = password1[0].isalpha()
#        if all(c.isalpha() == first_isalpha for c in password1):
#            raise forms.ValidationError("The new password must contain at least one letter and at least one digit or" \
#                                        " punctuation character.")
#
#        # ... any other validation you want ...
#
#        return password1
