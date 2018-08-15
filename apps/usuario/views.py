from django.shortcuts import render, redirect

from .forms import UsuarioForm, CuentaUsuarioForm

# Create your views here.

def principal(request):
    return render(request, 'principal/index.html')

def editar_usuario(request):
    return render(request, 'usuario/editar.html')


def registrar_usuario(request):
    if request.method == 'POST':
        formUsuario = UsuarioForm(request.POST, request.FILES)
        formCuenta = CuentaUsuarioForm(request.POST)
        context = {
            'formUsuario': formUsuario,
            'formCuenta': formCuenta,
            }
        if formUsuario.is_valid() and formCuenta.is_valid():
            usuario = formUsuario.save()
            cuenta = formCuenta.save(False)

            cuenta.usuario = usuario
            cuenta.save()

            return redirect('principal')
    else:
        formUsuario = UsuarioForm()
        formCuenta = CuentaUsuarioForm()

        context = {
            'formUsuario': formUsuario,
            'formCuenta': formCuenta,
        }

    return render(request, 'usuario/registrar.html', context=context)