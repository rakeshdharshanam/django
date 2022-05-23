from django.db import models
from django.core.validators import MaxLengthValidator , MinLengthValidator

# Create your models here.

class employee(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    # phone = models.IntegerField(validators=[MaxLengthValidator(10),MinLengthValidator(10)])