from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from course.models import Course
from student.models import Student
from .models import Enrollment
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
#read function
@login_required(login_url='login')
def create(request):
    if request.method == "POST":
        student_id = request.POST['student']
        course_id = request.POST['course']
        enr_date = request.POST['enr_date']
        try:
            student = Student.objects.get(pk=student_id) 
            course = Course.objects.get(pk=course_id)
        except Student.DoesNotExist and Course.DoesNotExist:
            # Handle the case where the department with the given ID doesn't exist
            messages.error(request, 'Invalid student or course selected.')
            return redirect("create_enr")
    
        Enrollment.objects.create(
            student=student,
            course=course,
            enr_date=enr_date
        )
        messages.success(request, 'enrollment added successfully.')
        return redirect("create_enr")
    else:  
        students = Student.objects.all()
        courses = Course.objects.all()
        context = {
            'students': students,
            'courses': courses
        }  
        return render(request, 'create_enr.html', context)

#read function
@login_required(login_url='login')
def read(request):
    enrollments = Enrollment.objects.all()
    context = {
        "enrs": enrollments
    }
    return render(request, 'read_enr.html', context)

#edit function
@login_required(login_url='login')
def edit(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == "POST":
        student_id = int(request.POST['student'])
        course_id = int(request.POST['course'])
        enr_date = request.POST['enr_date']

        enrollment.student_id=student_id
        enrollment.course_id=course_id
        enrollment.enr_date=enr_date
    
        enrollment.save()

        return redirect("read_enr")
    else:  
        students = Student.objects.all()
        courses = Course.objects.all()
        context = {
            'enr': enrollment,
            "students": students,
            'courses': courses,
        }
        return render(request, 'edit_enr.html', context)
    
#delete function
@login_required(login_url='login')
def delete(request, pk):
    enr = get_object_or_404(Enrollment, pk=pk)
    enr.delete()
    messages.success(request, 'Student deleted successfully.')

    return redirect("read_enr")