# Generated by Django 3.1.3 on 2020-11-29 15:13

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=70, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=70, unique=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default-avatar.jpg', upload_to='')),
                ('url', models.URLField(blank=True, max_length=300)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('country', models.CharField(blank=True, choices=[('CaC', 'Choose a Country'), ('Angola', 'Angola'), ('Afghanistan', 'Afghanistan'), ('Argentina', ' Argentina'), ('Algeria', 'Algeria'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Belgium', 'Belgium'), ('Burkinafaso', 'Burkina-Faso'), ('Botswana', 'Botswana'), ('Brazil', 'Brazil'), ('China', 'China'), ('Congo', 'Congo'), ('Cameroon', 'Cameroon'), ('Cuba', 'Cuba'), ('Denmark', 'Denmark'), ('Egypt', 'Egypt'), ('Ethiopia', 'Ethiopia'), ('Estonia', 'Estonia'), ('France', 'France'), ('Fiji', 'Fiji'), ('France', 'France'), ('Ghana', 'Ghana'), ('Gabon', 'Gabon'), ('Guinea', 'Guinea'), ('Germany', 'Germany'), ('Granada', 'Granada'), ('Hongkong', 'Hong-Kong'), ('Haiti', 'Haiti'), ('Hungary', 'Hungary'), ('Italy', 'Italy'), ('Indonesia', 'Indonesia'), ('Japan', 'Japan'), ('Kenya', 'Kenya'), ('Kuwait', 'Kuwait'), ('Liberia', 'Liberia'), ('Rwanda', 'Rwanda'), ('Sudan', 'Sudan'), ('Southafrica', 'South Africa'), ('Tanzania', 'Tanzania'), ('Uganda', 'Uganda')], default='CaC', max_length=100)),
                ('career', models.CharField(choices=[('Freelance', 'Individual / Freelance'), ('Agency', 'Agency - More than 10 people'), ('Studio', 'Studio - 10 people or fewer')], default='Freelance', max_length=100)),
                ('twitter', models.URLField(blank=True, default='https://twitter.com/')),
                ('facebook', models.URLField(blank=True, default='https://www.facebook.com/')),
                ('linkedin', models.URLField(blank=True, default='https://linkedin.com/')),
                ('instagram', models.URLField(blank=True, default='https://instagram.com/')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_joined',),
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitename', models.CharField(max_length=300)),
                ('siteurl', models.URLField(max_length=300)),
                ('siteimage', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('description', models.TextField(max_length=300)),
                ('technology', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(choices=[('CaC', 'Choose a Country'), ('Angola', 'Angola'), ('Afghanistan', 'Afghanistan'), ('Argentina', ' Argentina'), ('Algeria', 'Algeria'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Belgium', 'Belgium'), ('Burkinafaso', 'Burkina-Faso'), ('Botswana', 'Botswana'), ('Brazil', 'Brazil'), ('China', 'China'), ('Congo', 'Congo'), ('Cameroon', 'Cameroon'), ('Cuba', 'Cuba'), ('Denmark', 'Denmark'), ('Egypt', 'Egypt'), ('Ethiopia', 'Ethiopia'), ('Estonia', 'Estonia'), ('France', 'France'), ('Fiji', 'Fiji'), ('France', 'France'), ('Ghana', 'Ghana'), ('Gabon', 'Gabon'), ('Guinea', 'Guinea'), ('Germany', 'Germany'), ('Granada', 'Granada'), ('Hongkong', 'Hong-Kong'), ('Haiti', 'Haiti'), ('Hungary', 'Hungary'), ('Italy', 'Italy'), ('Indonesia', 'Indonesia'), ('Japan', 'Japan'), ('Kenya', 'Kenya'), ('Kuwait', 'Kuwait'), ('Liberia', 'Liberia'), ('Rwanda', 'Rwanda'), ('Sudan', 'Sudan'), ('Southafrica', 'South Africa'), ('Tanzania', 'Tanzania'), ('Uganda', 'Uganda')], default='CaC', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='category', to='awwards_users.category')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='awwards_users.profile')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
