from django.db import models
from django.db.models.fields import AutoField
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=500)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Create your models here.
class Medicamento(models.Model):
    id_medicamento = models.AutoField(primary_key=True)
    nombre_medicamento = models.CharField(max_length=40)
    descripcion = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField(default=0)
    concentracion = models.IntegerField()
    presentacion = models.IntegerField()
    url = models.ImageField(default='not_found')
    bioequivalente = models.ForeignKey('Bioequivalente', on_delete=models.CASCADE,default='')
    class Meta:
        db_table = "medicamento"
    def __str__(self):
        return "id_medicamento:"+id_medicamento+", nombre_medicamento"+nombre_medicamento+", descripcion"+descripcion+", precio"+precio+", url"+url+", concentracion"+concentracion+", presentacion"+presentacion



#TABLA DE BIOEQUIVALENCIA DE LOS MEDICAMENTOS, donde si el genero es 1, puede ser accion o 2 es rpg <- ejemplo
#Tabla de si es Bioequivalente o no
class Bioequivalente(models.Model):
    bioequivalente = models.CharField(max_length=100)
    class Meta:
        db_table = "bioequivalente"
    def __str__(self):
        return u'{0}'.format(self.bioequivalente)

#Tabla Farmacia
#class Farmacia(models.Model):
#    id_farmacia = models.AutoField(primary_key=True)
#    nombre_farmacia = models.CharField(max_length=40)
#    rut_farmacia = models.CharField(max_length=13)
#    direccion_farmacia = models.CharField(max_length=200)
#    class Meta:
#        db_table = "farmacia"
#    def __str__(self):
#        return "id_farmacia:"+id_farmacia+", nombre_farmacia"+nombre_farmacia+", rut_farmacia"+rut_farmacia+", direccion_farmacia"+direccion_farmacia



##Tabla Medicamento
#class Medicamento(models.Model):
#    	id_medicamento = models.AutoField(primary_key=True)
#    	nombre_medicamento = models.CharField(max_length=40)
#    	descripcion = models.TextField()
#    	precio = models.IntegerField()
##        concentracion = models.IntegerField()
#    	url = models.ImageField(default='not_found')
#    	stock = models.IntegerField(default=0)
#    	bioequivalente = models.ForeignKey('Bioequivalente', on_delete=models.CASCADE,default='')
##        id_farmacia_fk = models.ForeignKey('Farmacia', on_delete=models.CASCADE,default='')
#    	class Meta:
#        	db_table = "medicamento"
#    	def __str__(self):
#        	return "id_medicamento:"+id_medicamento+", nombre_medicamento"+nombre_medicamento+", descripcion"+descripcion+", precio"+precio+", url"+url