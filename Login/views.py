from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.template import Template, Context
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import *
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from .forms import UserCreationForm
import re

def loguearse(request):
    Logueo = AuthenticationForm()
    if request.method == 'POST':
        Logueo = AuthenticationForm(data=request.POST)
        nameUser = request.POST.get('username')
        namePassword = request.POST.get('password')
        if Logueo.is_valid():
            user = authenticate(request, username=nameUser, password=namePassword)
            if user is not None:
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
        password = request.POST.get('password1')
        validar = validar_contraseña(password)
        if Registrar.is_valid() and validar:
            Registrar.save()
            return redirect('/Login/RegistroCompleto')
        else:
            if not validar:
                messages = "La contraseña debe tener también al menos una mayúsucla y un número"
            else:
                messages = ""
            return render(request, 'Register.html',{'form': Registrar, 'mensaje':messages})
    else:
        Registrar = UserCreationForm()
        return render(request, 'Register.html', {'form': Registrar})
    
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

def validar_contraseña(password):
    caracter_presenta_mayus = False
    caracter_presenta_numero = False
    
    contrasena = password
    
    if re.search('[A-Z]',contrasena):
        caracter_presenta_mayus = True
        print(re.search('[A-Z]',contrasena))
    
    if re.search('[0-9]',contrasena):
        caracter_presenta_numero = True
        print(re.search('[0-9]',contrasena))
    
    if caracter_presenta_mayus and caracter_presenta_numero:
        print("Valido contraseña")
        return bool(True)
    else:
        return bool(False)