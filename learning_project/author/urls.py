from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('courses/<str:title>/', views.course, name='course')
]