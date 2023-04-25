from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),    
    path('addProduct/', views.addProduct, name='addProduct'),
    path('editProduct/<str:pk>/', views.editProduct, name='editProduct'),
    path('deleteProduct/<str:pk>/', views.deleteProduct, name='deleteProduct'),
    path('product//<str:pk>/', views.product, name='product'),
   path('addcart', views.addcart, name='addcart'),
    path('viewcart', views.viewcart, name='viewcart'), 
    path('updatecart', views.updatecart, name='updatecart'), 
    path('deletecart/<str:pk>', views.deletecart, name='deletecart'),       
    path('review/<str:pk>/', views.review, name='review'),   
    path('addRev/<str:pk>/', views.addRev, name='addReview'),
    path('editRev/<str:pk>/', views.editRev, name='editReview'),
    path('deleteReview/<int:pk>/', views.deleteReview, name='deleteReview'),
    path('contact/', views.contact, name='contact'),
    path('aboutus/', views.aboutus, name='aboutus'), 
     path('logout/', views.logout, name='logout'),   
]