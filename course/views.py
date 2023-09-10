from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Course
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
#read function
@login_required(login_url='login')
def create(request):
    if request.method == "POST":
        name = request.POST['name']
        cr_hrs = request.POST['credit']
    
        Course.objects.create(
            name=name,
            credit_hrs=cr_hrs
        )
        messages.success(request, 'Course added successfully.')
        return redirect("create_course")
    else:  
        return render(request, 'create_course.html')

#read function
@login_required(login_url='login')
def read(request):
    courses = Course.objects.all()
    context = {
        "courses": courses
    }
    return render(request, 'read_course.html', context)

#edit function
@login_required(login_url='login')
def edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        name = request.POST['name']
        cr_hrs = request.POST['cr_hrs']

        Course.name=name
        Course.credit_hrs=cr_hrs
    
        Course.save()

        return redirect("read_course")
    else:  
        return render(request, 'edit_course.html')
    
#delete function
@login_required(login_url='login')
def delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    messages.success(request, 'Course deleted successfully.')

    return redirect("read_course")