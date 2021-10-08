from django.db import models

class Tipo_Documento(models.Model):
    id_Type_Doc = models.IntegerField('Id tipo documento',primary_key=True)
    acronym     = models.CharField('Siglas',max_length=20)
    description = models.CharField('Descripcion',max_length=30)
    def __str__(self):
        return self.description

    class Meta:
        verbose_name ='Tipo de Documento'#nombre de la tabla
        verbose_name_plural ='Tipos de Documentos'
        db_table = 'Tipo_Documento'#Nombre de como aparecera en la base de datos
        ordering = ['id_Type_Doc']

class Rol(models.Model):
    id_Rol = models.IntegerField('Id rol',primary_key=True)
    description = models.CharField('Descripcion', max_length=30)
    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        db_table = 'Rol'
        ordering = ['id_Rol']

class Sede(models.Model):
    id_Campus     = models.IntegerField('Id sede',primary_key=True)
    name        = models.CharField('Nombre',max_length=100)
    location    = models.CharField('Ubicacion',max_length=100)
    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'Sede'
        verbose_name_plural = 'Sedes'
        db_table = 'Sede'
        ordering = ['id_Campus']

class nivel_Formacion(models.Model):
    Education_level = models.IntegerField('Nivel formacion',primary_key=True)
    description     = models.CharField("Descripcion",max_length=40)
    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'nivel_Formacion'
        verbose_name_plural = 'niveles de formacion'
        db_table = 'Nivel Formacion'
        ordering = ['Education_level']

class Jornada(models.Model):
    id_Working_Day    = models.IntegerField('Id Jornada',primary_key=True)
    description = models.CharField('Descripcion',max_length=30)
    start_time  = models.TimeField(' Hora de Inicio',max_length=30)
    final_hour  = models.TimeField('Hora Final',max_length=30)
    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'jornada'
        verbose_name_plural = 'jornadas'
        db_table = 'Jornada'
        ordering = ['id_Working_Day']
class Especialidad(models.Model):
    id_specialty =models.IntegerField('Especialidad',primary_key=True)
    description = models.CharField('Description',max_length=30)
    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'
        db_table = 'Especialidad'
        ordering = ['id_specialty']

class Usuario  (models.Model):
    type_Document = models.ForeignKey(Tipo_Documento,on_delete=models.CASCADE)
    id_User     = models.IntegerField('Usuario',primary_key=True)
    rol  = models.ForeignKey(Rol,on_delete=models.CASCADE)
    first_name  = models.CharField('Primer Nombre', max_length=30)
    second_name = models.CharField('Segundo Nombre', max_length=30,blank=True )
    surname     = models.CharField('Primer Apellido', max_length=30)
    second_surname = models.CharField('Segundo Apellido', max_length=30)
    email   = models.EmailField('Email', max_length=40)
    phone = models.IntegerField("Telefono")
    password    = models.CharField('Contraseña', max_length=20)
    photo = models.FileField(blank=True)
    def __int__(self):
        return self.id_User

    class Meta:
        verbose_name ='Usuario'
        verbose_name_plural ='Usuarios'
        db_table = 'Usuario'
        ordering = ['id_User']
class Usuario_Administrativo(models.Model):
    id_administrative = models.IntegerField('Id administrativo',primary_key=True)
    Id_Tipo_Doc_administrative = models.ForeignKey(Tipo_Documento, on_delete=models.CASCADE)
    def __str__(self):
        return self.id_administrative

    class Meta:
        verbose_name = 'Usuario Administrativo'
        verbose_name_plural = 'Usuarios Administrativos'
        db_table = 'Usuario Administrativo'
        ordering = ['id_administrative']

class usuario_aprendiz(models.Model):
    id_apprentice = models.IntegerField('Id aprendiz',primary_key=True)
    id_tipeDoc_apprentice = models.ForeignKey(Tipo_Documento,on_delete=models.CASCADE)
    def __int__(self):
        return self.id_apprentice

    class Meta:
        verbose_name='Usuario Aprendiz'
        verbose_name_plural = 'Usuarios Aprendices'
        db_table = 'Usuario Aprendiz'
        ordering = ['id_apprentice']

class Usuaro_Instructor(models.Model):
    id_instructor = models.IntegerField('Id instructor',primary_key=True)
    id_tipeDoc_instructor = models.ForeignKey(Tipo_Documento,on_delete=models.CASCADE)
    id_specialty = models.ForeignKey(Especialidad,on_delete=models.CASCADE)
    def __add__(self):
        return self.id_instructor +" " + self.id_tipeDoc_instructor

    class Meta:
        verbose_name='Usuario Instructor'
        verbose_name_plural = 'Usuarios Instructor'
        db_table = 'Usuario Instructor'
        ordering = ['id_instructor']

class Programa(models.Model):
    id_program  = models.IntegerField('Id programa',primary_key=True)
    name        = models.CharField('nombre',max_length=100)
    specialty_program = models.ForeignKey(Especialidad,on_delete=models.CASCADE)
    campus      = models.ForeignKey(Sede,on_delete=models.CASCADE)
    training_level = models.ForeignKey(nivel_Formacion,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Programa Academico'
        verbose_name_plural = 'Programas Academicos'
        db_table = 'Programa'
        ordering = ['id_program']

class ficha(models.Model):
    id_file     = models.IntegerField("Ficha",primary_key=True)
    id_program  = models.ForeignKey(Programa,on_delete=models.CASCADE)
    trimester   = models.IntegerField('Trimestre')
    working_day = models.ForeignKey(Jornada,on_delete=models.CASCADE)
    def __int__(self):
        return self.id_program

    class Meta:
        verbose_name='ficha'
        verbose_name_plural = 'fichas'
        db_table = 'Ficha'
        ordering = ['id_file']

class Asignacion_Ficha(models.Model):
    id_assignment = models.IntegerField("Id Asignacion",primary_key=True)
    id_file = models.ForeignKey(ficha,on_delete=models.CASCADE)
    id_user = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    def __str__(self):
        return self.id_assignment

    class Meta:
        verbose_name='Asignacion Ficha'
        verbose_name_plural = 'Asignaciones Fichas'
        db_table = 'Asignación'
        ordering = ['id_assignment']

class Registro_Asistencia(models.Model):
    id_register = models.IntegerField("Id registro",primary_key=True)
    registration_date = models.CharField('Fecha Registro',max_length=30)
    id_user_Register = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    rol_user = models.ForeignKey(Rol,on_delete=models.CASCADE)
    file = models.ForeignKey(ficha,on_delete=models.CASCADE)
    state = models.CharField('Estado',max_length=60 )
    novelty = models.CharField('Novedad',max_length=60)
    def __str__(self):
        return self.id_register
        
    class Meta:
        verbose_name='Registro_Asistencia'
        verbose_name_plural = 'Registros Asistencias'
        db_table = 'Reg. Asistencia'
        ordering = ['id_register']