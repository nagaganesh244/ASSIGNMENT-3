from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login , logout
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required


def home(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('verify')
    else:
        form = CustomUserCreationForm()
    return render(request , 'register.html',{"form": form})

def verify(request):
    return render(request , 'verify.html' )

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request , 'login.html',{'form': form})

def logout_view(request):
    if request.method =="POST":
        logout(request)
        return redirect('login')
    
@login_required(login_url='/login/') 
def dashboard(request):
    return render(request, 'dashboard.html')


