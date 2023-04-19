from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),    
    path('addProduct/', views.addProduct, name='addProduct'),
    path('editProduct/<str:pk>/', views.editProduct, name='editProduct'),
    path('deleteProduct/<str:pk>/', views.deleteProduct, name='deleteProduct'),
    path('product/', views.product, name='product'),     
    path('review/<str:pk>/', views.review, name='review'),   
    path('addRev/<str:pk>/', views.addRev, name='addReview'),
    path('editRev/<str:pk>/', views.editRev, name='editReview'),
    path('deleteReview/<int:pk>/', views.deleteReview, name='deleteReview'),
    path('contact/', views.contact, name='contact'),
    path('aboutus/', views.aboutus, name='aboutus'),   
]