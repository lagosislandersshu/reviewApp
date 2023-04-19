from django import forms
from users.models import Profile

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):   
    class Meta:
        model = Profile
        fields = ['dob', 'address', 'city', 'country', 'image']

        city = [
            ('', 'Select City'),
            ('Lagos', 'Lagos'),
            ('Abuja', 'Abuja'),
        ]

        country = [
            ('', 'Select Country'),
            ('Nigeria', 'Nigeria'),
            ('Ghana', 'Ghana'),
        ]

        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),
            'city':  forms.Select(choices=city, attrs={'type': 'select', 'class': 'form-control'}),
            'country':  forms.Select(choices=country, attrs={'type': 'select', 'class': 'form-control'}),
        }



