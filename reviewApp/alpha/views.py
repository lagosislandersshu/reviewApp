from django.shortcuts import render, redirect
from django.http import HttpResponse
from forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'alpha/home.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']            
            body = {
			'name': form.cleaned_data['name'],			 
			'email': form.cleaned_data['email_address'],             
			'message':form.cleaned_data['message'], 
			}
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, 'testing@example.com', ['testing@example.com'])
                messages.success(request, f'Thank you for contacting us')                
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ("contact")
        
    form = ContactForm()
        
    return render(request, "alpha/contact.html", {'form':form})

