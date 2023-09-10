from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from course.models import Course
from department.models import Department
from enrollment.models import Enrollment
from faculty.models import Faculty
from student.models import Student


def home(request):
    return render(request, 'index.html')


def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect("dashboard")
        
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username = username)
            
            if not user_obj.exists ():
                messages.info(request, "Account not Found")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            
            user_obj = authenticate(username = username, password = password)

            if user_obj and user_obj.is_superuser: 
                login(request, user_obj)
                return redirect("dashboard")
            
            messages.info(request, "Invalid Password!")
            return redirect('login')

        return render(request, 'login.html')
    
    except Exception as e:
        print(e)

def admin_logout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def dashboard(request):
    faculty_count = Faculty.objects.count()
    student_count = Student.objects.count()
    course_count = Course.objects.count()
    dept_count = Department.objects.count()
    enrollment_count = Enrollment.objects.count()

    context = {
        'faculty_count': faculty_count,
        'student_count': student_count,
        'course_count': course_count,
        'dept_count': dept_count,
        'enrollment_count': enrollment_count
    }
    
    return render(request, 'dashboard.html', context)