from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignUpForm(UserCreationForm):
    '''class to construct a sign up form'''

    first_name=forms.CharField(max_length=30,required=False)
    last_name=forms.CharField(max_length=30,required=False)
    email=forms.EmailField(max_length=254)

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']


class ProfileForm(forms.ModelForm):
    '''Class to create a form for profile objects'''

    class Meta:
        model=Profile
        fields=['name','about','facebook_profile','linkedin_profile','twitter_profile']


