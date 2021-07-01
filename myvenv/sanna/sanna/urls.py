"""sanna URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django import contrib
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
from blog import views
from django.contrib.auth import authenticate, views as auth_views

#REDIRECCIONAMIENTOS
urlpatterns = [
    path('admin/', admin.site.urls),
   
    #Crendeciales
    path('login',views.loginPage,name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('registro', views.registro,name="registro"),
#    path('accounts/',include('django.contrib.auth.urls')),
    #ADMINISTRACIÓN DE MEDICAMENTOS
    path('admin_medicamento', views.admin_medicamento, name="admin_medicamento"),
    path('crea_medicamento', views.crea_medicamento, name="crea_medicamento"),
    path('edita_medicamento/<int:id>', views.edita_medicamento),
    path('modificar/<int:id>',views.modificar),
    path('elimina_medicamento/<int:id>', views.elimina_medicamento),
    #LISTA DE MEDICAMENTOS
    path('medicamentos',views.medicamentos, name='medicamentos'), # <---- LISTA DE MEDICAMENTOS
    #CARPETA PRINCIPAL
    path('', views.index, name="index"),
    path('inicio', views.inicio, name="inicio"),
    path('acercade', views.acercade, name="acercade"),
    path('inicio_farmacia/<int:id>', views.inicio_farmacia, name="inicio_farmacia"),
    #PERFILES
    path('perfil_usuario', views.perfil_usuario, name="perfil_usuario"),
    path('perfil_admin/<int:id>', views.perfil_admin, name="perfil_admin"),
    path('modificar_perfil/<int:id>', views.modificar_perfil),
    #URLS ACTUALIZAR PASSWORD
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='Reset_password/password_reset.html'), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='Reset_password/password_reset_done.html'), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='Reset_password/password_reset_confirm.html'), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='Reset_password/password_reset_complete.html'), name="password_reset_complete"),    



    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
