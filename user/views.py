from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def register(request):
    
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        messages.success(request,"Başarıyla Giriş Yaptınız.")
        
        return redirect("index")
        
    context = {
        "form" : form
    }
    return render(request,"register.html",context)
def userLogin(request):

    form = LoginForm(request.POST or None)
    context = {
        "form" : form   
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Böyle Bir Kullanıcı Bulunmamaktadır.")
            return render(request,"login.html",context)

        login(request,user)
        messages.success(request,"Hoşgeldin, "+username)
        return redirect("index")

    return  render(request,"login.html",context)


        
def userLogout(request):
    logout(request)
    messages.success(request,"Sistemden çıkış yaptınız.")
    return redirect("index")