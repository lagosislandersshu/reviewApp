from django import forms
from alpha.models import Review
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Contact

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 50)
    email_address = forms.EmailField(max_length = 150)
    subject = forms.CharField(max_length = 150)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        name = forms.CharField(max_length=50)
        product_rating = forms.IntegerField()
        review_content = forms.CharField(widget = forms.Textarea, max_length=2000)      
       

        fields = ['name', 'product_rating', 'review_content']


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'    
        



