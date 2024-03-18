from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = [
    ('instructor', 'Instructor'),
    ('student', 'Student'),
]

class CustomUser(AbstractUser):
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='custom_user_set',  # Add a custom related_name
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set',  # Add a custom related_name
        related_query_name='user',
    )

class Courses(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True, null=True)


