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
    path('forgot_pass/',views.forgot_pass,name='forgot_pass'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name='register'),
    path('welcome/',views.welcome,name='welcome'),
    path('displaydata/',views.displaydata,name='displaydata'),
    path('emp_prof/',views.emp_prof,name='emp_prof'),
    path('insertdata/',views.insertdata,name='insertdata'),
    path('editdata/<int:id>',views.editdata,name='editdata'),
    path('deletedata/<int:id>',views.deletedata,name='deletedata'),
    path('change_pass/',views.change_pass,name='change_pass'),
    path('json_file/',views.json_file,name='json_file'),
    path('emailtemplate/', views.emailtemplate, name="emailtemplate"),
]
