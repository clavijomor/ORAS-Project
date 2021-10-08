from django.contrib import admin
from .models import Tipo_Documento,Rol,Sede,nivel_Formacion,Jornada,Especialidad,Usuario,Usuario_Administrativo,Usuaro_Instructor,usuario_aprendiz,Programa,ficha,Asignacion_Ficha,Registro_Asistencia

@admin.register(Tipo_Documento)
class Tipo_DocumentoAdmin(admin.ModelAdmin):
    list_display =("id_Type_Doc","description")
@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('id_Rol','description',)
@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    list_display =('id_Campus','name',)
@admin.register(nivel_Formacion)
class nivel_FormacionAdmin(admin.ModelAdmin):
    list_display =('Education_level','description',)
@admin.register(Jornada)
class JornadaAdmin(admin.ModelAdmin):
    list_display =('id_Working_Day','description',)
@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display =('id_specialty','description',)
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display =('type_Document','rol','first_name','second_name','surname','second_surname','email','phone','photo')
@admin.register(Usuario_Administrativo)
class Usuario_AdministrativoAdmin(admin.ModelAdmin):
    list_display =('id_administrative','Id_Tipo_Doc_administrative',)
@admin.register(Usuaro_Instructor)
class Usuaro_InstructorAdmin(admin.ModelAdmin):
    list_display =('id_instructor','id_tipeDoc_instructor','id_specialty',)
@admin.register(usuario_aprendiz)
class usuario_aprendizAdmin(admin.ModelAdmin):
    list_display =('id_apprentice','id_tipeDoc_apprentice',)
@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display =('id_program','name','specialty_program',)
@admin.register(ficha)
class fichaAdmin(admin.ModelAdmin):
    list_display =('id_file','id_program','trimester',)
@admin.register(Asignacion_Ficha)
class Asignacion_FichaAdmin(admin.ModelAdmin):
    list_display =('id_assignment','id_user',)
@admin.register(Registro_Asistencia)
class Registro_AsistenciaAdmin(admin.ModelAdmin):
    list_display =('id_register','registration_date','id_user_Register',)
# Register your models here.
