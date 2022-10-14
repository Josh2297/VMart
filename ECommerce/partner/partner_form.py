from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

# Forms Definition

class CustomCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=('username','email','password1','password2')
        widgets={'password1':forms.PasswordInput(attrs={'placeholder':'Enter Password'}),\
        'password2':forms.PasswordInput(attrs={'placeholder':'Re-Enter Password'}),\
        'email':forms.EmailInput(attrs={'placeholder':'Enter a Valid Email'})}

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=('first_name','last_name','gender','phone_no','state_of_origin','resident_state','home_address','occupation',\
            'profile_pic','region_of_del','location_of_del','transport_ques')
        widgets={'first_name':forms.TextInput(attrs={'placeholder':'Enter First Name'}),\
        'last_name':forms.TextInput(attrs={'placeholder':'Enter Last Name'}),\
        'username':forms.TextInput(attrs={'placeholder':'Enter UserName'}),\
        'home_address':forms.TextInput(attrs={'placeholder':'Home Address'})}
