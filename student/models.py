from django.db import models
from department.models import Department

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    cnic = models.CharField(max_length=13)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=11)
    dob = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
