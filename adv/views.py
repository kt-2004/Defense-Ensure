from django.http import Http404, HttpResponse
from django.shortcuts import render,redirect
from adv.models import Services, Guards, Contact, Users
from django.contrib import messages


def get_referer(request):
    referer = request.META.get('HTTP_REFERER')
    if not referer:
        return None
    return referer

# Create your views here.
def home(request):
    if "isLoggedIn" in request.session:
        listdata={"isLoggedIn":request.session["isLoggedIn"]}
        return render(request,"index.html",listdata)
    return render(request,"index.html")

def about(request):
    if "isLoggedIn" in request.session:
        listdata={"isLoggedIn":request.session["isLoggedIn"]}
        return render(request,"about.html",listdata)
    return render(request,"about.html")
def contact(request):
    if "isLoggedIn" in request.session:
        ls = {"success":False,"isLoggedIn":request.session["isLoggedIn"]}
    else:
        ls = {"success":False,"isLoggedIn":False}
    if request.method=='POST':
        name=request.POST['fname']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        formData=Contact(cName=name,cEmail=email,cPhone=phone,cMsg=message)
        formData.save()
        ls["success"] = True 
    return render(request,"contact.html",ls)
def guard(request):
    ls=Guards.objects.all()
    print(ls)
    if "isLoggedIn" in request.session: 
        listdataserver={
            'listdata':ls,
            'isLoggedIn':request.session["isLoggedIn"]
        }
    else:
        listdataserver={
            'listdata':ls,
            'isLoggedIn':False
        }
    return render(request,"guard.html",listdataserver)
def service(request):
    ls=Services.objects.all()
    print(ls)
    if "isLoggedIn" in request.session: 
        listdataserver={
            'listdata':ls,
            'isLoggedIn':request.session["isLoggedIn"]
        }
    else:
        listdataserver={
            'listdata':ls,
            'isLoggedIn':"False"
        }
    return render(request,"service.html",listdataserver)
def profile(request):
    return render(request,'profile.html')
def welcome(request):
    if not get_referer(request):
        return HttpResponse("<h1>Please Login first.</h1>")
    if "isLoggedIn" in  request.session:
        listdata={"isLoggedIn":request.session["isLoggedIn"]}
    else:
        listdata={"isLoggedIn":"False"}
    return render(request,'welcome.html',listdata)
def login(request):
    data={'login_failed':""}
    if request.method == 'POST' and request.POST['username']!="":
        user = request.POST['username']
        password=request.POST['password']
        ls=Users.objects.all()
        for i in ls:
            if user == i.uName:
                if password == i.uPass:
                    data['login_failed'] = "False"
                    request.session['isLoggedIn'] = "True"
                    return redirect("http://127.0.0.1:8000/welcome/")
        data['login_failed'] = "True"
    request.session['isLoggedIn'] = "False"
    return render(request,"login.html",data)
def logout(request):
    request.session["isLoggedIn"] = "False"
    return redirect("http://127.0.0.1:8000/home?logged_out")
def register(request):
    if request.method=='POST' and request.POST['username']!="":
        name=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        formData=Users(uName=name,uEmail=email,uPass=password)
        formData.save()
        return redirect("http://127.0.0.1:8000/login?registeration_success=true")
    return render(request,"registration.html")