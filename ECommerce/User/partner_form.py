from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

# Forms Definition

class CustomCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=('username','email','password1','password2','first_name','last_name','gender','phone_no','additional_phone_no','state_of_origin','resident_state','home_address','services',\
            'profile_pic','location_of_del','transport_ques')
        widgets={'password1':forms.PasswordInput(attrs={'placeholder':'Enter Password'}),\
        'password2':forms.PasswordInput(attrs={'placeholder':'Re-Enter Password'}),\
        'email':forms.EmailInput(attrs={'placeholder':'Enter a Valid Email'}),\
        'first_name':forms.TextInput(attrs={'placeholder':'Enter First Name'}),\
        'last_name':forms.TextInput(attrs={'placeholder':'Enter Last Name'}),\
        'username':forms.TextInput(attrs={'placeholder':'Enter UserName'}),\
        'home_address':forms.TextInput(attrs={'placeholder':'Home Address','required':True}),\
        'services':forms.TextInput(attrs={'required':True}),'profile_pic':forms.FileInput(attrs={'required':True}),'location_of_del':forms.TextInput(attrs={'required':True})}

    def clean_phone_no(self):
        value=self.cleaned_data.get('phone_no')
        if value.isdigit():
            return value
        else:
            raise ValidationError('Phone Number Should Contain Only Digits (0-9)')

    def clean_state_of_origin(self):
        value=self.cleaned_data.get('state_of_origin')
        if value:
            return value
        else:
            raise ValidationError('Pick an Option Fron The List')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=('first_name','last_name','gender','phone_no','additional_phone_no','state_of_origin','resident_state','home_address','services',\
            'profile_pic','location_of_del','transport_ques')
        widgets={'first_name':forms.TextInput(attrs={'placeholder':'Enter First Name'}),\
        'last_name':forms.TextInput(attrs={'placeholder':'Enter Last Name'}),\
        'username':forms.TextInput(attrs={'placeholder':'Enter UserName'}),\
        'home_address':forms.TextInput(attrs={'placeholder':'Home Address','required':True}),\
        'services':forms.TextInput(attrs={'required':True}),'profile_pic':forms.FileInput(attrs={'required':True}),'location_of_del':forms.TextInput(attrs={'required':True}),\
            }

    def clean_phone_no(self):
        value=self.cleaned_data.get('phone_no')
        if value.isdigit():
            return value
        else:
            raise ValidationError('Phone Number Should Contain Only Digits (0-9)')

    def clean_state_of_origin(self):
        value=self.cleaned_data.get('state_of_origin')
        if value:
            return value
        else:
            raise ValidationError('Pick an Option Fron The List')
