from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('courses/add_course/', views.add_course, name='add_course'),
    path('courses/delete_course/<int:course_id>', views.delete_course, name='delete_course'),
    path('courses/edit_course/<int:course_id>', views.edit_course, name='edit_course'),
    path('courses/<int:course_id>/', views.course, name='course'),
]