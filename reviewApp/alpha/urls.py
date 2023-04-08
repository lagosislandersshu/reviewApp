from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),    
    path('alpha/addProduct/', views.addProduct, name='addProduct'),
    path('alpha/editProduct/<int:pk>/', views.editProduct, name='editProduct'),
    path('alpha/deleteProduct/<int:pk>/', views.deleteProduct, name='deleteProduct'),
    path('alpha/product/', views.product, name='product'), 
    path('alpha/contact/', views.contact, name='contact'),
      
]