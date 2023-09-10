from django.shortcuts import render, get_object_or_404, redirect
from .models import Faculty
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from department.models import Department  # Import the Department model
from course.models import Course  # Import the Course model

# Create your views here.



@login_required(login_url='login')
def create(request):
    if request.method == "POST":
        name = request.POST['name']
        cnic = request.POST['cnic']
        email = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']
        department_id = request.POST['department']
        course_ids = request.POST.getlist('courses')  # Get selected course IDs as a list
        
        department = Department.objects.get(pk=department_id)
        
        faculty = Faculty.objects.create(
            name=name,
            cnic=cnic,
            email=email,
            phone=phone,
            dob=dob,
            department=department
        )
        
        # Assign selected courses to the faculty member
        for course_id in course_ids:
            faculty.courses.add(course_id)
        
        messages.success(request, 'Faculty member added successfully.')
        return redirect("create_faculty")
    else:
        # Retrieve a list of all available departments and courses
        departments = Department.objects.all()
        courses = Course.objects.all()
        context = {
            'departments': departments,
            'courses': courses
        }
        return render(request, 'create_faculty.html', context)

@login_required(login_url='login')
def read(request):
    faculty_members = Faculty.objects.all()
    context = {
        "faculty_members": faculty_members
    }
    return render(request, 'read_faculty.html', context)

@login_required(login_url='login')
def edit(request, pk):
    faculty_member = get_object_or_404(Faculty, pk=pk)
    if request.method == "POST":
        name = request.POST['name']
        cnic = request.POST['cnic']
        email = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']
        department_id = request.POST['department']
        course_ids = request.POST.getlist('courses')  # Get selected course IDs as a list

        department = Department.objects.get(pk=department_id)

        faculty_member.name = name
        faculty_member.cnic = cnic
        faculty_member.email = email
        faculty_member.phone = phone
        faculty_member.dob = dob
        faculty_member.department = department

        # Clear existing course assignments and assign selected courses
        faculty_member.courses.clear()
        for course_id in course_ids:
            faculty_member.courses.add(course_id)

        faculty_member.save()

        return redirect("read_faculty")
    else:
        # Retrieve a list of all available departments and courses
        departments = Department.objects.all()
        courses = Course.objects.all()
        context = {
            "faculty_member": faculty_member,
            "departments": departments,
            "courses": courses
        }
        return render(request, 'edit_faculty.html', context)

@login_required(login_url='login')
def delete(request, pk):
    faculty_member = get_object_or_404(Faculty, pk=pk)
    faculty_member.delete()
    messages.success(request, 'Faculty member deleted successfully.')

    return redirect("read_faculty")