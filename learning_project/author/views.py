from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth import authenticate, login, logout
from .models import Courses, CustomUser, Forum, Enrolled
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import CoursesForm, Question, Answer

def index(request):
    return render(request, 'author/index.html')

@login_required
def home(request):
    courses_id = []
    for enrollment in Enrolled.objects.filter(user=request.user):
        courses_id.append(enrollment.course.id)

    courses = []
    for course_id in courses_id:
        course = Courses.objects.get(id=course_id)
        courses.append(course)

    if request.user.is_authenticated:
        return render(request, 'author/home.html', {'courses': courses})
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
def delete_course(request, course_id):
    if request.user.role == "instructor":
        if request.method == 'POST':
            course = Courses.objects.get(id=course_id)
            course.delete()
            return redirect('courses')
    else:
        return redirect("index")


def edit_course(request, course_id):
    if request.user.role == "instructor":
        if request.method == "POST":
            form = CoursesForm(request.POST, instance=get_object_or_404(Courses, id=course_id))
            if form.is_valid():
                course = get_object_or_404(Courses, id=course_id)
                course.delete()
                form.save()
                return redirect('courses')
        else:
            form = CoursesForm(instance=get_object_or_404(Courses, id=course_id))

        return render(request, 'author/add_course.html', {'form': form})




@login_required
def add_course(request):
    if request.user.role == "instructor":
        if request.method == "POST":
            form = CoursesForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = CoursesForm()

        return render(request, 'author/add_course.html', {"form": form})
    else:
        return redirect("index")

@login_required
def forum(request):
    if request.user.role == "student":
        if request.method == "POST":
            form = Question(request.POST)
            if form.is_valid():
                form.save()
                return redirect("forum")
        else:
            form = Question()
        forum = Forum.objects.all()
        return render(request, 'author/forum.html', {'forum': forum, 'form': form})

    else:
        forum = Forum.objects.all()
        return render(request, 'author/forum.html', {'forum': forum})

@login_required
def answer(request, forum_id):
    if request.user.role == "instructor":
        if request.method == "POST":
            form = Answer(request.POST, instance=get_object_or_404(Forum, id=forum_id))
            if form.is_valid():
                answer = get_object_or_404(Forum, id=forum_id)
                answer.delete()
                form.save()
                return redirect("forum")
        else:
            form = Answer(instance=get_object_or_404(Forum, id=forum_id))

        forum = Forum.objects.all()
        return render(request, 'author/answer.html', {'form': form, 'forum': forum})

    else:
        return redirect("index")


@login_required
def enroll(request, course_id):
    course = get_object_or_404(Courses, id=course_id)
    if request.method == 'POST':
        if not Enrolled.objects.filter(user=request.user, course=course):
            Enrolled.objects.create(user=request.user, course=course)
        return redirect('home')
    return render(request, 'courses.html', {'course': course})
