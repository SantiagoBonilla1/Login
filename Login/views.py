from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.template import Template, Context
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


def loguearse(request):
    Logueo = AuthenticationForm()
    if request.method == 'POST':
        Logueo = AuthenticationForm(data=request.POST)
        name=request.POST.get('nombre_usuario')
        print(Logueo.is_valid)
        if Logueo.is_valid():
            return render(request, 'Inicio.html',{'Nombre': name, 'redireccionar':"true"})
        else:
            return render(request, 'Login.html',{'form': Logueo, 'mensaje_error':"Error"})
    else:
        return render(request, 'Login.html', {'form': Logueo})
    
def Inicio(request, username):
    return render(request, 'Inicio.html', {'nombre':username})

def Login(request):
    return render(request, 'Login.html')
    
def Registrarse(request):
    return render(request, 'Register.html')

def redirect_view_Login(request):
    return redirect('/Login/')

def redirect_view_Register(request):
    return redirect('/Registro/')