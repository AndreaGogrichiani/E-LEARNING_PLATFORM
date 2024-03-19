# Generated by Django 5.0.3 on 2024-03-19 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=400)),
                ('answer', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
    ]