from django.db import models

# Create your models here.
class task(models.Model):
    Name=models.CharField(max_length=20)
    task=models.CharField(max_length=1000)
    review=models.BooleanField(default=False)