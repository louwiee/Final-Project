from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from member_app.models import MemberProfile

from .forms import LoginForm, SignUpForm

# Create your views here.

def home(request):
    return render(request, 'rent.html')

def signup_acc(request):
    
    form = SignUpForm()

    if request.method == 'POST':
        
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('login')
    else:
        form = SignUpForm()
    
    return render(request, 'loginpage/signup.html', {'form': form})

def login_acc(request):
    
    form = LoginForm()

    if request.method == "POST":
        
        form = LoginForm(request.POST, request=request)
        
        if form.is_valid():
            
            login(request, form.user)

            

            return redirect("home")
        

    return render(request, 'loginpage/login.html', {'form':form})


def logout_acc(request):
    logout(request)
    return redirect('logout')


def profile_page(request,pk):
    
    #get user's movie rents
    user = request.user
    profile = MemberProfile.objects.get(user=user)
    

    return render(request, 'member_app/member.html', {'profile':profile})


