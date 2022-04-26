
from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    # path('index',views.index,name='home' ),
    # path('about',views.about,name='about' ),
    # path('services',views.services,name='services' ),
    # path('contact',views.services,name='contact' ),
    path('', views.search),
    path('searchusers/', views.searchusers),

    
]
