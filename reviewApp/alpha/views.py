from django.shortcuts import render, redirect
from django.http import HttpResponse
from alpha.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from .models import Product
import os

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

def addProduct(request):
    product = Product.objects.all()
    if request.method == "POST":
        prod = Product()        
        prod.name = request.POST.get('name')
        prod.brand = request.POST.get('brand')
        prod.average_cost = request.POST.get('average_cost')
        prod.category = request.POST.get('category')
        prod.date_released = request.POST.get('date_released')
        prod.desc = request.POST.get('desc')
        if len(request.FILES) != 0:
            prod.image = request.FILES['image']  
        prod.save()    
        messages.success(request, "Product Added Successfully")
        return redirect('addProduct')

    return render(request, 'alpha/add-product.html', {'product':product})

def editProduct(request, pk):
    prod = Product.objects.get(id=pk)
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(prod.image) > 0:
                os.remove(prod.image.path)
            prod.image = request.FILES['image']
        prod.name = request.POST.get('name')
        prod.brand = request.POST.get('brand')
        prod.average_cost = request.POST.get('average_cost')
        prod.category = request.POST.get('category')
        prod.date_released = request.POST.get('date_released')
        prod.desc = request.POST.get('desc')
        prod.save()
        messages.success(request, "Product Update was Successful")
        return redirect("addProduct") 
    
    context = {
        'prod': prod
    }
    return render(request, 'alpha/edit-product.html', context)

def deleteProduct(request, pk):
    prod = Product.objects.get(name=pk)
    if len(prod.image) > 0:
        os.remove(prod.image.path)
    prod.delete()
    messages.success(request, "Product delete was Successful")
    return redirect('addProduct')

def product(request):
    prod = Product.objects.all()
    context={
        'prod':prod
    }
    return render(request, 'alpha/product.html', context)



   
