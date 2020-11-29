# Generated by Django 3.1.3 on 2020-11-29 00:25

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default-avatar.jpg', upload_to='')),
                ('url', models.URLField(blank=True, max_length=300)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('country', models.CharField(blank=True, choices=[('CaC', 'Choose a Country'), ('Al', 'Angola'), ('Ag', 'Afghanistan'), ('Agt', ' Argentina'), ('Aga', 'Algeria'), ('Ata', 'Australia'), ('Au', 'Austria'), ('bg', 'Belgium'), ('bf', 'Burkina-Faso'), ('bt', 'Botswana'), ('bl', 'Brazil'), ('ch', 'China'), ('co', 'Congo'), ('ca', 'Cameroon'), ('cu', 'Cuba'), ('dk', 'Denmark'), ('eg', 'Egypt'), ('ep', 'Ethiopia'), ('es', 'Estonia'), ('fr', 'France'), ('fj', 'Fiji'), ('fr', 'France'), ('gh', 'Ghana'), ('ga', 'Gabon'), ('gu', 'Guinea'), ('ger', 'Germany'), ('gra', 'Granada'), ('hong', 'Hong-Kong'), ('ha', 'Haiti'), ('hung', 'Hungary'), ('itl', 'Italy'), ('ido', 'Indonesia'), ('jpn', 'Japan'), ('ke', 'Kenya'), ('ku', 'Kuwait'), ('li', 'Liberia'), ('rw', 'Rwanda'), ('su', 'Sudan'), ('sou', 'South Africa'), ('tz', 'Tanzania'), ('ug', 'Uganda')], default='CaC', max_length=100)),
                ('career', models.CharField(choices=[('Fl', 'Freelance'), ('Ag', 'Agency-More than 10 people'), ('St', 'Studio-10 people or fewer')], default='Fl', max_length=100)),
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
    ]
