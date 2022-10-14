from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
from django.utils import timezone

# Create your models here.
class CustomManager(UserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("Users Must Have an Email")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
    
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)
class CustomUser(AbstractUser):
    first_name=models.CharField(max_length=15,null=False,blank=False,default='')
    last_name=models.CharField(max_length=15,null=False,blank=False,default='')
    email=models.EmailField(verbose_name='Email Address',null=False,blank=False,unique=True)
    states_list=[(state.strip(),state.strip()) for state in open(r'C:\Users\DELL\Documents\states.txt')];states_list.sort();states_list=states_list[4:]
    gender_choices=[('male','Male'),('female','Female'),('Undefined','Prefer Not to Specify')]
    gender=models.CharField(max_length=10,verbose_name='Gender',choices=gender_choices)
    phone_no=models.IntegerField(verbose_name='Phone Number',null=True)
    home_address=models.CharField(max_length=20,null=True,blank=True)
    state_of_origin=models.CharField(max_length=50,verbose_name='State of Origin',choices=states_list)
    resident_state=models.CharField(max_length=50,verbose_name='State of Residence',choices=states_list)
    occupation=models.CharField(max_length=12,help_text='What Role will You Play?')
    profile_pic=models.ImageField(upload_to='profile_images',verbose_name='Upload a Profile Picture')
    location_of_del=models.CharField(max_length=20,verbose_name='Preferred Location of Delivery',help_text='This Location can be changed for Every Order Made')
    region_of_del=models.CharField(max_length=20,verbose_name='Preferred Region of Delivery',help_text='This Region can be changed for Every Order Made')
    transport_ques=models.BooleanField(null=True,blank=True,verbose_name='Can You Handle Transportation of Your Goods to Customers?')

    objects = CustomManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)

