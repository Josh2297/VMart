from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=('username','email','password1','password2','first_name','last_name','gender','phone_no','additional_phone_no',\
                'resident_state','home_address','location_of_del')
        widgets={'password1':forms.PasswordInput(attrs={'placeholder':'Enter Password'}),\
        'password2':forms.PasswordInput(attrs={'placeholder':'Re-Enter Password'}),\
        'email':forms.EmailInput(attrs={'placeholder':'Enter a Valid Email'}),\
        'first_name':forms.TextInput(attrs={'placeholder':'Enter First Name'}),\
        'last_name':forms.TextInput(attrs={'placeholder':'Enter Last Name'}),\
        'username':forms.TextInput(attrs={'placeholder':'Enter UserName'}),\
        'home_address':forms.TextInput(attrs={'placeholder':'Home Address'})}

    def clean_phone_no(self):
        value=self.cleaned_data.get('phone_no')
        if value.isdigit():
            return value
        else:
            raise ValidationError('Phone Number Should Contain Only Digits (0-9)')



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=('first_name','last_name','gender','phone_no','additional_phone_no','resident_state','home_address',\
            'location_of_del')
        widgets={'first_name':forms.TextInput(attrs={'placeholder':'Enter First Name'}),\
        'last_name':forms.TextInput(attrs={'placeholder':'Enter Last Name'})}

    def clean_phone_no(self):
        value=self.cleaned_data.get('phone_no')
        if value.isdigit():
            return value
        else:
            raise ValidationError('Phone Number Should Contain Only Digits (0-9)')
