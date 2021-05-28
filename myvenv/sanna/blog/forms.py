from django import forms
from django.db.models import fields
from blog.models import User
from django import forms

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'