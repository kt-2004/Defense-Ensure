from django.contrib import admin
from django.urls import path
from adv import views
from adv import admin
urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.home, name=''),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('guard/',views.guard,name='guard'),
    path('service/',views.service, name='service'),     
    path('profile/',views.profile,name='profile'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name='register'),
    path('welcome/',views.welcome,name='welcome')
]
