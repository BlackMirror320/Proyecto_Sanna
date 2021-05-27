from django.db import models
from django.utils import timezone

from django.db.backends.mysql import models
class Medicine(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "medicamentos"

# Create your models here.
