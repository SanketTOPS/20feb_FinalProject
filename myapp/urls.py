from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.index),
    path('login/',views.login,name='login'),
    path('signup/',views.signup),
    path('notes/',views.notes),
    path('about/',views.about),
    path('contact/',views.contact),
    path('otpverify/',views.otpverify,name='otpverify'),
    path('userlogout/',views.userlogout),
    path('profile/',views.profile),
]
