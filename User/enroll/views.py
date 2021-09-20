from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import  authenticate,login,logout
# Create your views here.

# sign up
def sign_up(request):
    if request.method=="POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Successfully!!')
            fm.save()
            return render(request,'enroll/signup.html',{'form':fm})
        else:
            return render(request,'enroll/signup.html',{'form':fm})
    else:        

        fm=SignUpForm()    
        return render(request,'enroll/signup.html',{'form':fm})    


# login
def user_login(request):    
    if request.method=="POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,pasword=upass)
            if user is not None:
                login(request, user)
            return HttpResponseRedirect('/profile/')
        else:
            fm=AuthenticationForm()
    fm=AuthenticationForm()        
    return render(request,'enroll/userlogin.html', {'form':fm})


# profile
def user_profile(request):
    return render(request,'enroll/profile.html',)

# logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')