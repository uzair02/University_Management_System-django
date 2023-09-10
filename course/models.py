from django.db import models
from faculty.models import Faculty

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    credit_hrs = models.PositiveIntegerField()
    faculty = models.ManyToManyField(Faculty, related_name='courses')