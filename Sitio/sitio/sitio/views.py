from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib import messages

def Aprendiz_Vista(request):
    return render(request,'Aprendiz_Vista.html')
def Cambiar_defini_instructor(request):
    return render(request,'Cambiar_defini_instructor.html')
def cambiar_definir(request):
    return render(request,'cambiar_definir.html')
def cambio_de_clave_admin(request):
    return render(request,'cambio_de_clave_admin.html')
def cambio_de_clave_aprendiz(request):
    return render(request,'cambio_de_clave_aprendiz.html')
def cambio_de_clave_instructor(request):
    return render(request,'cambio_de_clave_instructor.html')
def FormRegistroUsuarios(request):
    return render(request,'FormRegistroUsuarios.html')
def Generador_de_informes(request):
    return render(request,'Generador_de_informes.html')
def Generador_vista_estudiante(request):
    return render(request,'Generador_vista_estudiante.html')
def gestionDeConsultas(request):
    return render(request,'gestionDeConsultas.html')
def gestion_consultas_informes_individuales_SupU(request):
    return render(request,'gestion_consultas_informes_individuales_SupU.html')
def Gestion_consultas_SuperU(request):
    return render(request,'Gestion_consultas_SuperU.html')
def gestion_de_consultas_de_informes_generales(request):
    return render(request,'gestion_de_consultas_de_informes_generales.html')
def Gestions_consulta_generales_Superu(request):
    return render(request,'Gestions_consulta_generales_Superu.html')
def index(request):
    return render(request,'index.html')
def ingresosAdministrativosORAS(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request,'Usuario correcto')
            return redirect('http://127.0.0.1:8000/Super_Usuario_Vista')
        else:
            messages.error(request,"Usuario o contraseña incorrecta")
    return render(request, 'ingresosAdministrativosORAS.html',{
    })
def ingreso_aprendiz(request):
    return render(request,'ingreso_aprendiz.html')
def ingresoInstructor(request):
    return render(request,'ingresoInstructor.html')
def instructor_vista_Uno(request):
    return render(request, 'instructor_vista_Uno.html')
def ListaDeAprendices(request):
    return render(request,'ListaDeAprendices.html')
def listado_aprendices_superu(request):
    return render(request,'listado_aprendices_superu.html')
def listado_novedades_superu(request):
    return render(request,'listado_novedades_superu.html')
def Listados_y_Novedades(request):
    return render(request,'Listados_y_Novedades.html')
def Mis_Actividades(request):
    return render(request,'Mis_Actividades.html')
def Mis_Actividades_Aprend(request):
    return render(request,'Mis_Actividades_Aprend.html')
def Perfil_Sistema_Aprendiz(request):
    return render(request,'Perfil_Sistema_Aprendiz.html')
def Perfil_Sistema_Instructor(request):
    return render(request,'Perfil_Sistema_Instructor.html')
def Perfil_sistema_SuperU(request):
    return render(request,'Perfil_sistema_SuperU.html')
def recuerda_contraseña_admin(request):
    return render(request,'recuerda_contraseña_admin.html')
def recuerda_contraseña_aprendiz(request):
    return render(request,'recuerda_contraseña_aprendiz.html')
def recuerda_contraseña_instructor(request):
    return render(request,'recuerda_contraseña_instructor.html')
def Registro_Aprendiz(request):
    return render(request,'Registro_Aprendiz.html')
def Registro_Instructor(request):
    return render(request,'Registro_Instructor.html')
def Registro_Manual(request):
    return render(request,'Registro_Manual.html')
def registro_novedades_Usperu(request):
    return render(request,'Registro_novedades_Usperu.html')
def registro_Novedaes(request):
    return render(request,'registro_Novedaes.html')
def Super_Usuario_Vista(request):
    return render(request,'Super_Usuario_Vista.html')
def gestion_de_consultas_de_informes_individuales(request):
    return render(request,'gestion_de_consultas_de_informes_individuales.html')
def inicio(request):
    return render(request,'inicio.html')