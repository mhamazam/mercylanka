from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request,'index.html')

def handlesignup(request):
    if request.method=='POST':
        fullname=request.POST.get("fullname")
        uname=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("pass1")
        confirmpassword=request.POST.get("pass2")
        try:
            if User.objects.get(username=uname):
                return HttpResponse("User Name is already taken")
        except:
            pass
        try:
            if User.objects.get(email=email):
                return HttpResponse("Email is already taken")
        except:
            pass
        myuser=User.objects.create_user(username=uname,email=email,password=password)
        myuser.first_name = fullname
        myuser.save()
        return redirect('handlesignin')
    return render(request,'signup.html')

def handlesignin(request):
    return render(request,'signin.html')

def handlesignout(request):
    return render(request,'logout.html')