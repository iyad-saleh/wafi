from django import forms
from django.conf import settings
from .models import MyUser
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2',
                  'first_name','last_name','avatar','is_MANAGER',
                  'is_RESERVATION','is_ACCOUNTANT','is_CUSTOMER']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = MyUser
        fields = ['username', 'email','is_MANAGER',
                  'first_name','last_name','is_RESERVATION',
                   'is_ACCOUNTANT','is_CUSTOMER']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','phoneNumber']
