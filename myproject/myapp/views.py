from django.http import HttpResponse 
from django.shortcuts import render
from django.contrib.auth import  authenticate , login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm , UserRegistrationForm
from .models import Profile



# Create your views here.

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'] , password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("user successfully loged in")
                else:
                    return HttpResponse("disabld the account")
            else:
                return HttpResponse ("invalid login")
    else:
        form = LoginForm()
    return render(request, 'myapp/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request,'myapp/dashboard.html',{'section': 'dashboard'})


def register(request):
    user_form = UserRegistrationForm()
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'myapp/registration_done.html', {'new_user': new_user})
        else:
            user_form = UserRegistrationForm()
    return render(request, 'myapp/register.html', {'user_form':user_form})