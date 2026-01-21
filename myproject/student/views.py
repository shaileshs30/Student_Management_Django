from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from .forms import StudentForm
from .models import Student,StudentProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('student_list')
        return render(request, 'student/login.html', {
            'error': 'Invalid credentials'
        })
    return render(request, 'student/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def user_signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return redirect('login')
    return render(request, 'student/signup.html')

    
def student_list(request):
    student = Student.objects.all()
    return render(request,'student/student_list.html', {'student':student})

def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save() 
        return redirect('student_list')
    return render(request,'student/student_form.html',{'form':form})

def student_update(request,id):
    student = get_object_or_404(Student,id=id)
    form = StudentForm(request.POST or None,instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request,'student/student_form.html',{'form':form})

def student_delete(request,id):
    student = get_object_or_404 (Student,id=id)
    if request.method =="POST":
        student.delete()
        return redirect('student_list')
    return render(request,'student/student_confirm_delete.html',{'student':student})

def student_profile(request,id):
    student = get_object_or_404(Student, id=id)
    if request.method =="POST":
        address = request.POST.get ("address")
        image =  request.FILES.get("profile_image")
        StudentProfile.objects.update_or_create(
            student=student,
            defaults={
                "address":address,
                "profile_image":image
            }
        )
        return redirect('student_detail',id=student.id)
    return render (request,'student/profile_form.html',{'student':student})


def student_detail(request,id):
    student= get_object_or_404 (Student ,id=id)
    return render(request,'student/student_detail.html',{'student':student})
# # Create your views here.
