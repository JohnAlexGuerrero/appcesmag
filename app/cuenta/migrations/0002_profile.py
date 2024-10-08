# Generated by Django 5.1 on 2024-08-22 17:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.SmallIntegerField(blank=True, choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='número de contacto')),
                ('ocupacion', models.CharField(blank=True, choices=[('Profesional', 'Profesional'), ('Estudiante', 'Estudiante'), ('Desarrollador', 'Desarrollado')], max_length=150, null=True)),
                ('academia', models.CharField(blank=True, max_length=150, null=True)),
                ('slug', models.SlugField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
