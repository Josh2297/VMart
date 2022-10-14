from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
from django.utils import timezone
from PIL import Image

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
    id=models.CharField(max_length=50,primary_key=True)
    first_name=models.CharField(max_length=15,null=False,blank=False,default='')
    last_name=models.CharField(max_length=15,null=False,blank=False,default='')
    email=models.EmailField(verbose_name='Email Address',null=False,blank=False,unique=True)
    states_list=[(state.strip(),state.strip()) for state in open(r'C:\Users\DELL\Documents\states.txt')];states_list.sort();states_list=states_list[4:]
    gender_choices=[('male','Male'),('female','Female'),('none','Prefer Not to Specify')]
    gender=models.CharField(max_length=10,verbose_name='Gender',choices=gender_choices)
    phone_no=models.CharField(verbose_name='Phone Number',max_length=15)
    additional_phone_no=models.CharField(help_text='Add an additional Phone Number (Optional)',max_length=15,null=True,blank=True)
    home_address=models.CharField(max_length=20,null=True,blank=True,help_text='Home Address is Optional')
    state_of_origin=models.CharField(max_length=50,verbose_name='State of Origin',choices=states_list,null=True,blank=True,help_text='Optional')
    resident_state=models.CharField(max_length=50,verbose_name='State of Residence',choices=states_list)
    services=models.CharField(max_length=15,help_text='What Services do you intend to offer Play?',null=True,blank=True)
    profile_pic=models.ImageField(upload_to='profile_images',verbose_name='Upload a Profile Picture',null=True,blank=True)
    location_of_del=models.CharField(max_length=20,null=True,blank=True,verbose_name='Preferred Location of Delivery',help_text='This Location can be changed for Every Order Made')
    transport_ques=models.BooleanField(null=True,blank=True,verbose_name='Can You Handle Transportation of Your Goods to Customers?')
    status_list=(('pending','Pending'),('approved','Approved'),('not_approved','Not Approved'))
    partnership_status=models.CharField(max_length=15,choices=status_list,help_text="Status of Partner Request",null=True,blank=True)

    objects = CustomManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)

    def save (self):
        super().save()
        img=Image.open(self.profile_pic.path)
        #Resize It
        if img.height >300 or img.width >300:
            output_size=(400,400)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)
