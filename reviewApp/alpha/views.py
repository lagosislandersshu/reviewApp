from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import ContactForm, ReviewForm
from django.core.mail import send_mail, BadHeaderError
from .models import Product, Review
from django.core.paginator import Paginator
from django.contrib import messages
import os

# Create your views here.
def home(request):    
    return render(request, 'alpha/home.html')

def aboutus(request):    
    return render(request, 'alpha/aboutus.html')

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

# view all product...
def product(request):     
    p = Paginator(Product.objects.all(), 4)
    page = request.GET.get('page')
    prod = p.get_page(page)
    prod2= Product.objects.all().count()   
    
    return render(request, 'alpha/product.html',{'prod':prod, 'prod2':prod2 })

@login_required
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

@login_required
def editProduct(request, pk):
    prod = Product.objects.get(name=pk)
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


@login_required
def deleteProduct(request, pk):
    prod = Product.objects.get(name=pk)
    if len(prod.image) > 0:
        os.remove(prod.image.path)
    prod.delete()
    messages.success(request, "Product delete was Successful")
    return redirect('addProduct')

def review(request, pk):
    prod = Product.objects.get(name=pk)   
    p = Paginator(Review.objects.filter(name=pk), 2)
    page = request.GET.get('page')
    review = p.get_page(page)
    userid = request.user.id
    review2 = Review.objects.filter(author=userid, name=pk).count()    
    return render(request, 'alpha/review.html', {'prod':prod, 'review':review, 'review2':review2 })


@login_required
def addRev(request, pk):
    review = Product.objects.get(name=pk)    
    if request.method=="POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
           reviewpost = form.save(commit=False)
           reviewpost.author = request.user
           reviewpost.save()

           return redirect('review', pk)
    else:
        form=ReviewForm()    
    return render(request, 'alpha/addReview.html', {'review':review })

@login_required
def editRev(request, pk):
    review = Review.objects.get(name=pk, author=request.user)        
    if request.method=="POST":        
        review.author = request.user
        review.name = request.POST.get('name')
        review.product_rating = request.POST.get('product_rating')
        review.review_content = request.POST.get('review_content')   
        review.save()
        return redirect('review', review.name)
   
    return render(request, 'alpha/editReview.html', {'review':review})


@login_required
def deleteReview(request, pk):
    prod = Review.objects.get(id=pk)
    prod.delete()
    messages.success(request, "Review delete was Successful")
    return redirect('review', prod.name)
   

   
