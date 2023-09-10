from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from department.models import Department
from .models import Student
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
#read function
@login_required(login_url='login')
def create(request):
    if request.method == "POST":
        name = request.POST['name']
        cnic = request.POST['cnic']
        email = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']
        department_id = request.POST['department']

        try:
            department = Department.objects.get(pk=department_id)  # Retrieve the Department instance
        except Department.DoesNotExist:
            # Handle the case where the department with the given ID doesn't exist
            messages.error(request, 'Invalid department selected.')
            return redirect("create_student")
    
        Student.objects.create(
            name=name,
            cnic=cnic,
            email=email,
            phone=phone,
            dob=dob,
            department=department
        )
        messages.success(request, 'Student added successfully.')
        return redirect("create_student")
    else:  
        dept = Department.objects.all()
        context = {
            'dept': dept,
        }  
        return render(request, 'create_student.html', context)

#read function
@login_required(login_url='login')
def read(request):
    students = Student.objects.all()
    context = {
        "students": students
    }
    return render(request, 'read_student.html', context)

#edit function
@login_required(login_url='login')
def edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        name = request.POST['name']
        cnic = request.POST['cnic']
        email = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']
        department_id = int(request.POST['department'])

        student.name=name
        student.cnic=cnic
        student.email=email
        student.phone=phone
        student.dob=dob
        student.department_id=department_id
    
        student.save()

        return redirect("read_student")
    else:  
        dept = Department.objects.all()
        context = {
            "student": student,
            'dept': dept,
        }
        return render(request, 'edit_student.html', context)
    
#delete function
@login_required(login_url='login')
def delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    messages.success(request, 'Student deleted successfully.')

    return redirect("read_student")