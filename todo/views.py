from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


# Create your views here
def home(request):
    return render(request, 'todo/home.html')


def singupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/singupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/singupuser.html',
                              {'form': UserCreationForm(),
                               'error': "That username has already been taken. Please, choose a new username"})
        else:
            return render(request, 'todo/singupuser.html',
                          {'form': UserCreationForm(), 'error': "Password did't match"})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if not user:
            return render(request, 'todo/loginuser.html',
                          {'form': AuthenticationForm(), 'error': "Username and password didn't match"})
        else:
            login(request, user)
            return redirect('currenttodos')

def currenttodos(request):
    return render(request, 'todo/currenttodos.html')
