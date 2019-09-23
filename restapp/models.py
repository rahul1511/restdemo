from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=25)
    empid=models.IntegerField()
    email=models.EmailField(max_length=25)
    location=models.CharField(max_length=10)
    salery=models.DecimalField(max_digits=10, decimal_places=3)
    def __str__(self):
        return f"{self.name}"
