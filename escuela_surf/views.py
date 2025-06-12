from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import RegistroUsuarioForm, EditarAlumnoForm, EditarUsuarioForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Alumno, Clase
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'escuela_surf/index.html')

def registro_alumno(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            telefono = form.cleaned_data.get('telefono')
            direccion = form.cleaned_data.get('direccion')
            fecha_nacimiento = form.cleaned_data.get('fecha_nacimiento')

            
            Alumno.objects.create(
                user=user,
                telefono=telefono,
                direccion=direccion,
                fecha_nacimiento=fecha_nacimiento
            )

            login(request, user)  
            return redirect('login')  
    else:
        form = RegistroUsuarioForm()

    return render(request, 'escuela_surf/registro_alumno.html', {'form': form})

def vista_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect('perfil_alumno')
        else:
            username = request.POST.get('username')
            if not User.objects.filter(username=username).exists():
                messages.warning(request, "El usuario no existe. Por favor, regístrate.")
                
            else:
                messages.warning(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()

    return render(request, 'escuela_surf/login.html', {'form': form})

@login_required
@login_required
def perfil_alumno(request):
    alumno = request.user.alumno  # Relación OneToOne con User

    # Membresía activa más reciente
    membresia_activa = alumno.membresia_set.filter(activa=True).order_by('-fecha_inicio').first()

    # Clases asignadas al alumno
    clases_asignadas = alumno.clases.all().order_by('dia', 'hora_inicio')

    context = {
        'alumno': alumno,
        'membresia': membresia_activa,
        'clases': clases_asignadas,  # esto lo agregamos
    }
    return render(request, 'escuela_surf/perfil_alumno.html', context)


@login_required
def editar_perfil(request):
    usuario = request.user
    alumno = usuario.alumno

    if request.method == 'POST':
        form_usuario = EditarUsuarioForm(request.POST, instance=usuario)
        form_alumno = EditarAlumnoForm(request.POST, instance=alumno)

        if form_usuario.is_valid() and form_alumno.is_valid():
            form_usuario.save()
            form_alumno.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('perfil_alumno')
    else:
        form_usuario = EditarUsuarioForm(instance=usuario)
        form_alumno = EditarAlumnoForm(instance=alumno)

    return render(request, 'escuela_surf/editar_perfil.html', {
        'form_usuario': form_usuario,
        'form_alumno': form_alumno
    })