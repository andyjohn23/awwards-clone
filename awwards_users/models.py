from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from cloudinary.models import CloudinaryField
from PIL import Image

# Create your models here.


class ManagerAccount(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('users must have an emailaddress')
        if not username:
            raise ValueError('users must have a username')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )

        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=70, unique=True)
    username = models.CharField(max_length=70, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = ManagerAccount()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Profile(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    image = models.ImageField(default='default-avatar.jpg')
    url = models.URLField(max_length=300, blank=True)
    description = models.TextField(max_length=200, blank=True)

    Freelance = 'Fl'
    Agency = 'Ag'
    Studio = 'St'

    CAREER_CHOICES = [
        (Freelance, 'Individual / Freelance'),
        (Agency, 'Agency - More than 10 people'),
        (Studio, 'Studio - 10 people or fewer'),
    ]
    Country = 'CaC'
    Angola = 'Al'
    Afghanistan = 'Ag'
    Argentina = 'Agt'
    Algeria = 'Aga'
    Australia = 'Ata'
    Austria = 'Au'
    Belgium = 'bg'
    Burkinafaso = 'bf'
    Botswana = 'bt'
    Brazil = 'bl'
    China = 'ch'
    Congo = 'co'
    Cameroon = 'ca'
    Cuba = 'cu'
    Denmark = 'dk'
    Egypt = 'eg'
    Ethiopia = 'ep'
    Estonia = 'es'
    France = 'fr'
    Fiji = 'fj'
    Finland = 'fl'
    Ghana = 'gh'
    Gabon = 'ga'
    Guinea = 'gu'
    Germany = 'ger'
    Granada = 'gra'
    Hongkong = 'hong'
    Haiti = 'ha'
    Hungary = 'hung'
    Italy = 'itl'
    Indonesia = 'ido'
    Japan = 'jpn'
    Kenya = 'ke'
    Kuwait = 'ku'
    Liberia = 'li'
    Rwanda = 'rw'
    Sudan = 'su'
    Southafrica = 'sou'
    Uganda = 'ug'
    Tanzania = 'tz'

    COUNTRY_CHOICES = [
        (Country, 'Choose a Country'),
        (Angola, 'Angola'),
        (Afghanistan, 'Afghanistan'),
        (Argentina, ' Argentina'),
        (Algeria, 'Algeria'),
        (Australia, 'Australia'),
        (Austria, 'Austria'),
        (Belgium, 'Belgium'),
        (Burkinafaso, 'Burkina-Faso'),
        (Botswana, 'Botswana'),
        (Brazil, 'Brazil'),
        (China, 'China'),
        (Congo, 'Congo'),
        (Cameroon, 'Cameroon'),
        (Cuba, 'Cuba'),
        (Denmark, 'Denmark'),
        (Egypt, 'Egypt'),
        (Ethiopia, 'Ethiopia'),
        (Estonia, 'Estonia'),
        (France, 'France'),
        (Fiji, 'Fiji'),
        (France, 'France'),
        (Ghana, 'Ghana'),
        (Gabon, 'Gabon'),
        (Guinea, 'Guinea'),
        (Germany, 'Germany'),
        (Granada, 'Granada'),
        (Hongkong, 'Hong-Kong'),
        (Haiti, 'Haiti'),
        (Hungary, 'Hungary'),
        (Italy, 'Italy'),
        (Indonesia, 'Indonesia'),
        (Japan, 'Japan'),
        (Kenya, 'Kenya'),
        (Kuwait, 'Kuwait'),
        (Liberia, 'Liberia'),
        (Rwanda, 'Rwanda'),
        (Sudan, 'Sudan'),
        (Southafrica, 'South Africa'),
        (Tanzania, 'Tanzania'),
        (Uganda, 'Uganda'),
    ]

    country = models.CharField(
        default=Country, choices=COUNTRY_CHOICES, max_length=100, blank=True)
    career = models.CharField(
        default=Freelance, choices=CAREER_CHOICES, max_length=100, blank=False)
    twitter = models.URLField(
        default='https://twitter.com/', max_length=200, blank=True)
    facebook = models.URLField(
        default='https://www.facebook.com/', max_length=200, blank=True)
    linkedin = models.URLField(
        default='https://linkedin.com/', max_length=200, blank=True)
    instagram = models.URLField(
        default='https://instagram.com/', max_length=200, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering = ('-date_joined',)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Projects(models.Model):
    sitename = models.CharField(max_length=300, blank=False, null=False)
    siteurl = models.URLField(max_length=300, blank=False, null=False)
    siteimage = CloudinaryField('image')
    category = models.ForeignKey(
        'Category', on_delete=models.PROTECT, blank=False, related_name='category')
    description = models.TextField(max_length=300, blank=False, null=False)
    technology = models.CharField(max_length=100, blank=True, null=True)
    profile = models.ForeignKey(
        'Profile', on_delete=models.CASCADE, related_name='projects')

    Country = 'CaC'
    Angola = 'Al'
    Afghanistan = 'Ag'
    Argentina = 'Agt'
    Algeria = 'Aga'
    Australia = 'Ata'
    Austria = 'Au'
    Belgium = 'bg'
    Burkinafaso = 'bf'
    Botswana = 'bt'
    Brazil = 'bl'
    China = 'ch'
    Congo = 'co'
    Cameroon = 'ca'
    Cuba = 'cu'
    Denmark = 'dk'
    Egypt = 'eg'
    Ethiopia = 'ep'
    Estonia = 'es'
    France = 'fr'
    Fiji = 'fj'
    Finland = 'fl'
    Ghana = 'gh'
    Gabon = 'ga'
    Guinea = 'gu'
    Germany = 'ger'
    Granada = 'gra'
    Hongkong = 'hong'
    Haiti = 'ha'
    Hungary = 'hung'
    Italy = 'itl'
    Indonesia = 'ido'
    Japan = 'jpn'
    Kenya = 'ke'
    Kuwait = 'ku'
    Liberia = 'li'
    Rwanda = 'rw'
    Sudan = 'su'
    Southafrica = 'sou'
    Uganda = 'ug'
    Tanzania = 'tz'

    COUNTRY_CHOICES = [
        (Country, 'Choose a Country'),
        (Angola, 'Angola'),
        (Afghanistan, 'Afghanistan'),
        (Argentina, ' Argentina'),
        (Algeria, 'Algeria'),
        (Australia, 'Australia'),
        (Austria, 'Austria'),
        (Belgium, 'Belgium'),
        (Burkinafaso, 'Burkina-Faso'),
        (Botswana, 'Botswana'),
        (Brazil, 'Brazil'),
        (China, 'China'),
        (Congo, 'Congo'),
        (Cameroon, 'Cameroon'),
        (Cuba, 'Cuba'),
        (Denmark, 'Denmark'),
        (Egypt, 'Egypt'),
        (Ethiopia, 'Ethiopia'),
        (Estonia, 'Estonia'),
        (France, 'France'),
        (Fiji, 'Fiji'),
        (France, 'France'),
        (Ghana, 'Ghana'),
        (Gabon, 'Gabon'),
        (Guinea, 'Guinea'),
        (Germany, 'Germany'),
        (Granada, 'Granada'),
        (Hongkong, 'Hong-Kong'),
        (Haiti, 'Haiti'),
        (Hungary, 'Hungary'),
        (Italy, 'Italy'),
        (Indonesia, 'Indonesia'),
        (Japan, 'Japan'),
        (Kenya, 'Kenya'),
        (Kuwait, 'Kuwait'),
        (Liberia, 'Liberia'),
        (Rwanda, 'Rwanda'),
        (Sudan, 'Sudan'),
        (Southafrica, 'South Africa'),
        (Tanzania, 'Tanzania'),
        (Uganda, 'Uganda'),
    ]
    country = models.CharField(
        default=Country, choices=COUNTRY_CHOICES, max_length=100, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.sitename)

    class Meta:
        ordering = ('-created',)
