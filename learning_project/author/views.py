from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from .models import Courses, CustomUser
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import CoursesForm

def index(request):
    return render(request, 'author/index.html')

def home(request):
    if request.user.is_authenticated:
        return render(request, 'author/home.html')
    else:
        return redirect("index")

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'author/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()

    return render(request, 'author/login.html', {"form": form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def courses(request):
    courses = Courses.objects.all()
    return render(request, 'author/courses.html', {"courses": courses})

@login_required
def course(request, course_id):
    courses = []

    for i in Courses.objects.all():
        courses.append(i.id)

    if course_id in courses:
        course = Courses.objects.get(id=course_id)
        return render(request, 'author/course.html', {'course': course})

    else:
        return redirect("index")


@login_required
def add_course(request):
    if request.user.role == "instructor":
        if request.method == "POST":
            form = CoursesForm(request.POST)
            if form.is_valid():
                course = form.save()
                return redirect('home')
        else:
            form = CoursesForm()

        return render(request, 'author/add_course.html', {"form": form})
    else:
        return redirect("index")
