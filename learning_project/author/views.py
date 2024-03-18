from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from .models import Courses

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

def user_logout(request):
    logout(request)
    return redirect('login')

def courses(request):
    courses = Courses.object.all()
    return render(request, 'author/courses.html', {"courses": courses})
