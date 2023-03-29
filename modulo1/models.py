# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alarma(models.Model):
    idalarmas = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    estado = models.IntegerField()
    fecha_de_la_alarma = models.DateField(db_column='fecha de la alarma')  # Field renamed to remove unsuitable characters.
    rutasonido = models.CharField(max_length=45)
    talarma_idtalarma = models.ForeignKey('Talarma', models.DO_NOTHING, db_column='talarma_idtalarma')
    calarma_idcalarma = models.ForeignKey('Calarma', models.DO_NOTHING, db_column='calarma_idcalarma')

    class Meta:
        managed = False
        db_table = 'alarma'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Calarma(models.Model):
    idcalarma = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'calarma'


class Collar(models.Model):
    idcollar = models.AutoField(primary_key=True)
    talla = models.CharField(max_length=2)
    color = models.CharField(max_length=45)
    material = models.CharField(max_length=45)
    forma = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'collar'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empresa(models.Model):
    idempresa = models.AutoField(primary_key=True)
    nit = models.CharField(unique=True, max_length=45)
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    telefono = models.IntegerField()
    persona_idpersona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='persona_idpersona')

    class Meta:
        managed = False
        db_table = 'empresa'


class Especie(models.Model):
    idespecie = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'especie'


class Evento(models.Model):
    idevento = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'evento'


class Fcabeza(models.Model):
    idfactura = models.AutoField(primary_key=True)
    fechacompra = models.DateField(blank=True, null=True)
    descuento = models.IntegerField()
    iva = models.IntegerField()
    preciototalapagar = models.IntegerField()
    persona_idpersona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='persona_idpersona')
    tdocumento_idtdocumento = models.ForeignKey('Tdocumento', models.DO_NOTHING, db_column='tdocumento_idtdocumento')
    fechadeventa = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fcabeza'


class Fcuerpo(models.Model):
    idfcuerpo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    cantidad = models.IntegerField()
    precioventa = models.IntegerField()
    fcabeza_idfactura = models.ForeignKey(Fcabeza, models.DO_NOTHING, db_column='fcabeza_idfactura')

    class Meta:
        managed = False
        db_table = 'fcuerpo'


class Geolocalizacion(models.Model):
    idgeolocalizacion = models.AutoField(primary_key=True)
    fecha = models.DateField()
    longitud = models.FloatField()
    latitud = models.FloatField()
    collar_idcollar = models.ForeignKey(Collar, models.DO_NOTHING, db_column='collar_idcollar')

    class Meta:
        managed = False
        db_table = 'geolocalizacion'


class Historial(models.Model):
    idhistorialdelocalizacion = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    geolocalizacion_idgeolocalizacion = models.ForeignKey(Geolocalizacion, models.DO_NOTHING, db_column='geolocalizacion_idgeolocalizacion')
    alarma_idalarmas = models.ForeignKey(Alarma, models.DO_NOTHING, db_column='alarma_idalarmas')
    evento_idevento = models.ForeignKey(Evento, models.DO_NOTHING, db_column='evento_idevento')

    class Meta:
        managed = False
        db_table = 'historial'


class Inventario(models.Model):
    idinventario = models.AutoField(primary_key=True)
    #producto=models.CharField(max_length=100)
    cantinicial = models.IntegerField()
    cantactual = models.IntegerField()
    fechacompra = models.DateField()
    precioventa = models.IntegerField()
    persona_idpersona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='persona_idpersona')

    class Meta:
        managed = False
        db_table = 'inventario'


class Mascota(models.Model):
    idmascota = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    color = models.CharField(max_length=45)
    peso = models.CharField(max_length=45)
    genero = models.CharField(max_length=45)
    fechadenacimiento = models.DateField()
    foto = models.CharField(max_length=90, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    collar_idcollar = models.ForeignKey(Collar, models.DO_NOTHING, db_column='collar_idcollar')
    tanimal_idtanimal = models.ForeignKey('Tanimal', models.DO_NOTHING, db_column='tanimal_idtanimal')
    raza_idraza = models.ForeignKey('Raza', models.DO_NOTHING, db_column='raza_idraza')
    especie_idespecie = models.ForeignKey(Especie, models.DO_NOTHING, db_column='especie_idespecie')
    alarma_idalarmas = models.ForeignKey(Alarma, models.DO_NOTHING, db_column='alarma_idalarmas')

    class Meta:
        managed = False
        db_table = 'mascota'


class Persona(models.Model):
    idpersona = models.AutoField(primary_key=True)
    identificacion = models.CharField(max_length=10)
    primernombre = models.CharField(max_length=45)
    segundonombre = models.CharField(max_length=45, blank=True, null=True)
    primerapellido = models.CharField(max_length=45)
    segundoapellido = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=45)
    tpersona_idtpersona = models.ForeignKey('Tpersona', models.DO_NOTHING, db_column='tpersona_idtpersona')
    tdocumento_idtdocumento = models.ForeignKey('Tdocumento', models.DO_NOTHING, db_column='tdocumento_idtdocumento')

    class Meta:
        managed = False
        db_table = 'persona'


class Raza(models.Model):
    idraza = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'raza'


class Relacion(models.Model):
    idrelacion = models.AutoField(primary_key=True)
    persona_idpersona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='persona_idpersona')
    mascota_idmascota = models.ForeignKey(Mascota, models.DO_NOTHING, db_column='mascota_idmascota')

    class Meta:
        managed = False
        db_table = 'relacion'


class Talarma(models.Model):
    idtalarma = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'talarma'


class Tanimal(models.Model):
    idtanimal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tanimal'


class Tdocumento(models.Model):
    idtdocumento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tdocumento'


class Tpersona(models.Model):
    idtpersona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tpersona'
