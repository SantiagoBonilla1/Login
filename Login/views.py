from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.template import Template, Context
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import *
from .forms import UserCreationForm
from datetime import date, timedelta
import re

def loguearse(request):
    Logueo = AuthenticationForm()
    if request.method == 'POST':
        Logueo = AuthenticationForm(data=request.POST)
        nameUser = request.POST.get('username')
        namePassword = request.POST.get('password')
        if Logueo.is_valid():
            user = authenticate(username=nameUser, password=namePassword)
            if user is not None:
                if date.today() - user.password_date > timedelta(days=30):
                    return redirect('/password_reset/')
                else:
                    login(request, user)
                    request.session['nombre'] = nameUser
                    return redirect('/Inicio/')
            else:
                return render(request, 'Login.html',{'form': Logueo})
        else:
            return render(request, 'Login.html',{'form': Logueo})
    else:
        return render(request, 'Login.html', {'form': Logueo})

def Registrarse(request):
    if request.method == 'POST':
        Registrar = UserCreationForm(data=request.POST)
        if Registrar.is_valid():
            Registrar.save()
            return redirect('/Login/RegistroCompleto')
        else:
            messages = ""
            return render(request, 'Register.html',{'form': Registrar, 'mensaje':messages})
    else:
        Registrar = UserCreationForm()
        return render(request, 'Register.html', {'form': Registrar})

def LoginComplete(request):
    print(request.POST.get('username'))
    return redirect('/Login/')

def Logout(request):
    logout(request)
    return redirect('/Login/')

def Inicio(request):
    return render(request, 'Inicio.html')

def Login(request):
    Logueo = AuthenticationForm()
    return render(request, 'Login.html', {'form': Logueo})

def redirect_view_Login(request):
    return redirect('/Login/')

def redirect_view_Register(request):
    return redirect('/Registro/')

def redirect_view_Inicio(request):
    return redirect('/Inicio/')
