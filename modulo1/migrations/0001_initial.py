# Generated by Django 4.1.3 on 2022-11-08 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alarma',
            fields=[
                ('idalarmas', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('estado', models.IntegerField()),
                ('fecha_de_la_alarma', models.DateField(db_column='fecha de la alarma')),
                ('rutasonido', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'alarma',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Calarma',
            fields=[
                ('idcalarma', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'calarma',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Collar',
            fields=[
                ('idcollar', models.AutoField(primary_key=True, serialize=False)),
                ('talla', models.CharField(max_length=2)),
                ('color', models.CharField(max_length=45)),
                ('material', models.CharField(max_length=45)),
                ('forma', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'collar',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('idempresa', models.AutoField(primary_key=True, serialize=False)),
                ('nit', models.CharField(max_length=45, unique=True)),
                ('nombre', models.CharField(max_length=45)),
                ('direccion', models.CharField(max_length=45)),
                ('telefono', models.IntegerField()),
            ],
            options={
                'db_table': 'empresa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('idespecie', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'especie',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('idevento', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'evento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fcabeza',
            fields=[
                ('idfactura', models.AutoField(primary_key=True, serialize=False)),
                ('fechacompra', models.DateField(blank=True, null=True)),
                ('descuento', models.IntegerField()),
                ('iva', models.IntegerField()),
                ('preciototalapagar', models.IntegerField()),
                ('fechadeventa', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'fcabeza',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fcuerpo',
            fields=[
                ('idfcuerpo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('cantidad', models.IntegerField()),
                ('precioventa', models.IntegerField()),
            ],
            options={
                'db_table': 'fcuerpo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Geolocalizacion',
            fields=[
                ('idgeolocalizacion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('longitud', models.FloatField()),
                ('latitud', models.FloatField()),
            ],
            options={
                'db_table': 'geolocalizacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('idhistorialdelocalizacion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'historial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('idinventario', models.AutoField(primary_key=True, serialize=False)),
                ('cantinicial', models.IntegerField()),
                ('cantactual', models.IntegerField()),
                ('fechacompra', models.DateField()),
                ('precioventa', models.IntegerField()),
            ],
            options={
                'db_table': 'inventario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('idmascota', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('color', models.CharField(max_length=45)),
                ('peso', models.CharField(max_length=45)),
                ('genero', models.CharField(max_length=45)),
                ('fechadenacimiento', models.DateField()),
                ('foto', models.CharField(blank=True, max_length=90, null=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'mascota',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('idpersona', models.AutoField(primary_key=True, serialize=False)),
                ('identificacion', models.CharField(max_length=10)),
                ('primernombre', models.CharField(max_length=45)),
                ('segundonombre', models.CharField(blank=True, max_length=45, null=True)),
                ('primerapellido', models.CharField(max_length=45)),
                ('segundoapellido', models.CharField(blank=True, max_length=45, null=True)),
                ('email', models.CharField(max_length=45)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'persona',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('idraza', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'raza',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Relacion',
            fields=[
                ('idrelacion', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'relacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Talarma',
            fields=[
                ('idtalarma', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'talarma',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tanimal',
            fields=[
                ('idtanimal', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'tanimal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tdocumento',
            fields=[
                ('idtdocumento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'tdocumento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tpersona',
            fields=[
                ('idtpersona', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'tpersona',
                'managed': False,
            },
        ),
    ]
