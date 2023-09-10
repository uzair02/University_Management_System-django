from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Department
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
#read function
@login_required(login_url='login')
def create_dept(request):
    if request.method == "POST":
        name = request.POST['name']
        Department.objects.create(
            name=name
        )
        messages.success(request, 'Department added successfully.')
        return redirect("create_dept")
    else:    
        return render(request, 'create_dept.html')

#read function
@login_required(login_url='login')
def read_dept(request):
    dept = Department.objects.all()
    context = {
        "dept": dept
    }
    return render(request, 'read_dept.html', context)

#edit function
@login_required(login_url='login')
def edit_dept(request, pk):
    dept = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        name = request.POST['name']

        dept.name=name
    
        dept.save()

        return redirect("read_dept")
    else:  
        context = {
            "dept": dept
        }
        return render(request, 'edit_dept.html', context)
    
#delete function
@login_required(login_url='login')
def delete_dept(request, pk):
    dept = get_object_or_404(Department, pk=pk)
    dept.delete()
    messages.success(request, 'Department deleted successfully.')

    return redirect("read_dept")