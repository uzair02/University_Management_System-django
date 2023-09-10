from django.db import models
from course.models import Course
from student.models import Student

# Create your models here.
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enr_date = models.CharField(max_length=10)