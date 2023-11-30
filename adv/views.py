from django.http import HttpResponse
from django.shortcuts import render,redirect
from adv.models import Services, Guards, Contact, Users,Employee
from adv.form import EmployeeForm
from django.contrib import messages
import requests
import json
from django.core.mail import EmailMessage

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
def login(request):#names refrence from Users model
    data={'login_failed':""}
    if request.method == 'POST' and request.POST['uName']!="":
        uName = request.POST['uName']
        uPass=request.POST['uPass']
        ls=Users.objects.all()
        for i in ls:
            if uName == i.uName:
                if uPass == i.uPass:
                    data['login_failed'] = "False"
                    request.session['isLoggedIn'] = "True"
                    request.session['username'] = uName
                    return redirect("http://127.0.0.1:8000/welcome/")
        data['login_failed'] = "True"
    request.session['isLoggedIn'] = "False"
    return render(request,"login.html",data)
def logout(request):
    request.session["isLoggedIn"] = "False"
    request.session["username"] = ""
    return redirect("http://127.0.0.1:8000/home?logged_out")
def register(request):#names  refrence from Users model
    if request.method=='POST' and request.POST['uName']!="":
        uName=request.POST['uName']
        uEmail=request.POST['uEmail']
        uPass=request.POST['uPass']
        formData=Users(uName=uName,uEmail=uEmail,uPass=uPass)
        formData.save()
        request.session['username'] =uName
        return redirect("http://127.0.0.1:8000/login?registeration_success=true")
    return render(request,"registration.html")
def displaydata(request):
    if not get_referer(request):
        return HttpResponse("<h1>Please Login first.</h1>")
    listform=Employee.objects.all()
    lsdata={
        'listformdata':listform
    }
    if "isLoggedIn" in request.session:
        lsdata["isLoggedIn"] = request.session["isLoggedIn"]
    return render(request,"displaydata.html",lsdata)
def insertdata(request):
    if not get_referer(request):
        return HttpResponse("<h1>Please Login first.</h1>")
    form=EmployeeForm
    if request.method == 'POST':
        submitform=form(request.POST)
        submitform.save()
        return redirect('http://127.0.0.1:8000/displaydata/')
    else:
        return render(request,"insertdata.html",{'formfield':form})
def editdata(request,id):
    if not get_referer(request):
        return HttpResponse("<h1>Please Login first.</h1>")
    up=Employee.objects.get(eId=id)
    if request.method == 'POST':
        up=Employee.objects.get(eId=id)
        submitform=EmployeeForm(request.POST,instance=up)
        submitform.save()
        return redirect('http://127.0.0.1:8000/displaydata/')
    else:
        #return redirect('login')
        return render(request,"editdata.html",{'editf':up})    
def deletedata(request,id):
    if not get_referer(request):
        return HttpResponse("<h1>Please Login first.</h1>")
    up=Employee.objects.get(eId=id)
    up.delete()
    return redirect('http://127.0.0.1:8000/displaydata/')
    

def emp_prof(request):
    if not get_referer(request):
        return HttpResponse("<h1>Please Login first.</h1>")
    listdata={}
    if request.method=="POST":
        uEmail = request.POST['uEmail']
        emp=Users.objects.get(uName=request.session['username'])
        emp.uEmail=uEmail
        emp.save()
    if "username" in request.session:
        try:
            emp=Users.objects.get(uName=request.session['username'])
            listdata['editf'] = emp
        except:
            pass
    if "isLoggedIn" in request.session:
        listdata["isLoggedIn"] = request.session["isLoggedIn"]
    else:
        listdata['isLoggedIn'] = "False"
    return render(request,"emp_prof.html",listdata)


def change_pass(request):
    if not get_referer(request):
        return HttpResponse("<h1>Please Login first.</h1>")
    listdata={}
    if request.method=="POST":
        uName = request.POST['uName']
        request.session['username'] = uName
        uPass= request.POST['uPass']
        ch=Users.objects.get(uName=request.session['username'])
        ch.uPass=uPass
        ch.uName=uName
        ch.save()
        return redirect("http://127.0.0.1:8000/change_pass/?password_changed=true")
    if "username" in request.session:
        try:
            ch=Users.objects.get(uName=request.session['username'])
            listdata['editf'] = ch
        except:
            pass   
    if "isLoggedIn" in request.session:
        listdata["isLoggedIn"] = request.session["isLoggedIn"]
    else:
        listdata['isLoggedIn'] = "False"
    return render(request,"change_pass.html",listdata)

def forgot_pass(request):
    if request.method=="POST":
        uName = request.POST['uName']
        uPass = request.POST['newPass']
        try:
            ch=Users.objects.get(uName=uName)
        except:
            return redirect("http://127.0.0.1:8000/forgot_pass/?invalid_username=true")
        ch.uPass=uPass
        ch.save()
        return redirect("http://127.0.0.1:8000/login/")
    return render(request,"forgot_pass.html")

def json_file(request):
    response=requests.get("https://jsonplaceholder.typicode.com/users")
    users=response.json()
    listdata = {}
    listdata["users"] = users
    if "isLoggedIn" in request.session:
        listdata["isLoggedIn"] = request.session["isLoggedIn"]
    else:
        listdata['isLoggedIn'] = "False"
    return render(request,"json_file.html",listdata) 
       
def emailtemplate(request):
    email = EmailMessage('Leave Application', 'Hello,I am writing this mail for applying 3 days leave as I have to visit Bangalore for Visa-related process.',to=['khushithakar016@gmail.com'])
    email.send()
    return render(request, "emailtemplate.html")