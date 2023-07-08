from django.shortcuts import render , redirect,HttpResponseRedirect
from django.contrib.auth import login , logout , authenticate
from django.contrib import messages
from .models import *



def admin_signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        re_password = request.POST.get("re_password")
 
        admin = CustomUser.objects.filter(email = email)
        if admin.exists():
            messages.warning(request,'Email Already exist!')
            return HttpResponseRedirect(request.path_info)
        elif password != re_password:
            messages.warning(request,'Password Matching Error!')
            return HttpResponseRedirect(request.path_info)
        else:
            admin = CustomUser.objects.create(username = name,email=email,is_admin=True,is_customer =False)
            admin.set_password(password)
            admin.save()
            login(request,admin)
            return redirect('home')
    return render(request,'accounts/admin_signup.html',context={'title':'Town Foods Admin | Sign Up'})

def admin_login(request):
    if request.method == "POST":
        Email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request,email=Email , password=password)
        print(user)
        if user is not None and user.is_admin:
            login(request,user)
            return redirect('home')
        elif user is not None and not user.is_admin:
            messages.warning(request,'Invalid Account!')
        else:
            messages.warning(request,'Invalid Email or Password!')
    return render(request,'accounts/admin_login.html',context={'title':'Town Foods Admin | Log In'})

def admin_logout(request):
    request.session.clear()
    logout(request)
    return redirect('admin_login')

def customer_sign_up(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email= request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        if password != re_password:
            messages.warning(request,"Passwords Matching Error!")
            return HttpResponseRedirect(request.path_info)
        user = CustomUser.objects.filter(email = email)
        if user.exists():
            messages.warning(request,"Email Already Exist!")
            return HttpResponseRedirect(request.path_info)
        user = CustomUser.objects.create(username = name , email = email,is_admin=False,is_customer =True)
        user.set_password(password)
        user.save()
        login(request,user)
        return redirect('home_page')   
    return render(request,'accounts/signup.html',context={'current_page':'signup','title':'Town Foods | Customer Sign Up'})

def customer_log_in(request):
    if request.method == "POST":
        Email = request.POST.get('email')
        Password = request.POST.get('password')
        print(Email,Password)
        user = authenticate(email = Email,password = Password)
        if user is not None and user.is_customer:
            login(request,user)
            return redirect('home_page')  
        elif user is not None and not user.is_customer:
            messages.warning(request,'Invalid Account!')
        else:
            messages.warning(request,'Invalid Email Or Password!')
    return render(request,'accounts/login.html',context={'current_page':'login','title':'Town Foods | Customer Login'})

def customer_log_out(request):
    request.session.clear()
    logout(request)
    return redirect('home_page')
