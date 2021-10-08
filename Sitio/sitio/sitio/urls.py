"""sitio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('Aprendiz_Vista',views.Aprendiz_Vista),
    path('instructor_vista_Uno',views.instructor_vista_Uno),
    path('Cambiar_defini_instructor',views.Cambiar_defini_instructor),
    path('cambiar_definir',views.cambiar_definir),
    path('cambio_de_clave_admin',views.cambio_de_clave_admin),
    path('cambio_de_clave_aprendiz',views.cambio_de_clave_aprendiz),
    path('cambio_de_clave_instructor',views.cambio_de_clave_instructor),
    path('FormRegistroUsuarios',views.FormRegistroUsuarios),
    path('Generador_de_informes',views.Generador_de_informes),
    path('Generador_vista_estudiante',views.Generador_vista_estudiante),
    path('gestionDeConsultas',views.gestionDeConsultas),
    path('gestion_consultas_informes_individuales_SupU',views.gestion_consultas_informes_individuales_SupU),
    path('Gestion_consultas_SuperU',views.Gestion_consultas_SuperU),
    path('gestion_de_consultas_de_informes_generales',views.gestion_de_consultas_de_informes_generales),
    path('Gestions_consulta_generales_Superu',views.Gestions_consulta_generales_Superu),
    path('ingresosAdministrativosORAS',views.ingresosAdministrativosORAS),
    path('ingreso_aprendiz',views.ingreso_aprendiz),
    path('ingresoInstructor',views.ingresoInstructor),
    path('instructor_vista_Uno',views.instructor_vista_Uno),
    path('ListaDeAprendices',views.ListaDeAprendices),
    path('listado_aprendices_superu',views.listado_aprendices_superu),
    path('listado_novedades_superu',views.listado_novedades_superu),
    path('Listados_y_Novedades',views.Listados_y_Novedades),
    path('Mis_Actividades_Aprend',views.Mis_Actividades_Aprend),
    path('Mis_Actividades',views.Mis_Actividades),
    path('Perfil_Sistema_Aprendiz',views.Perfil_Sistema_Aprendiz),
    path('Perfil_Sistema_Instructor',views.Perfil_Sistema_Instructor),
    path('Perfil_sistema_SuperU',views.Perfil_sistema_SuperU),
    path('recuerda_contraseña_admin',views.recuerda_contraseña_admin),
    path('recuerda_contrasena_aprendiz',views.recuerda_contrasena_aprendiz),
    path('recuerda_contraseña_instructor',views.recuerda_contraseña_instructor),
    path('Registro_Aprendiz',views.Registro_Aprendiz),
    path('Registro_Instructor',views.Registro_Instructor),
    path('Registro_Manual',views.Registro_Manual),
    path('registro_novedades_Usperu',views.registro_novedades_Usperu),
    path('registro_Novedaes',views.registro_Novedaes),
    path('Super_Usuario_Vista',views.Super_Usuario_Vista),
    path('gestion_de_consultas_informes_individuales',views.gestion_de_consultas_de_informes_individuales),
    path('inicio',views.inicio)
]
