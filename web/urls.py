
from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('', views.home,name='home'),
    path('handlesignup', views.handlesignup,name='handlesignup'),
    path('handlesignin', views.handlesignin,name='handlesignin'),
    path('handlesignout', views.handlesignout,name='handlesignout'),
    
]
