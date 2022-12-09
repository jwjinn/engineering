# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Academy(models.Model):
    academy_name = models.CharField(primary_key=True, max_length=100)
    lesson_category = models.CharField(max_length=50)
    academy_address = models.CharField(max_length=200)
    lesson_fee = models.BigIntegerField()
    lesson_hours = models.BigIntegerField()
    gugun = models.ForeignKey('SeoulInfo', models.DO_NOTHING, db_column='Gugun')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'academy'
        unique_together = (('academy_name', 'academy_address'),)


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


class Bus(models.Model):
    bus_station_id = models.CharField(primary_key=True, max_length=100)
    sido = models.CharField(max_length=50)
    gugun = models.ForeignKey('SeoulInfo', models.DO_NOTHING, db_column='gugun')

    class Meta:
        managed = False
        db_table = 'bus'


class CoreCity(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    population = models.PositiveIntegerField()
    country = models.ForeignKey('CoreCountry', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'core_city'


class CoreCountry(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'core_country'


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


class DjangoPlotlyDashDashapp(models.Model):
    id = models.BigAutoField(primary_key=True)
    instance_name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=110)
    base_state = models.TextField()
    creation = models.DateTimeField()
    update = models.DateTimeField()
    save_on_change = models.IntegerField()
    stateless_app = models.ForeignKey('DjangoPlotlyDashStatelessapp', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_plotly_dash_dashapp'


class DjangoPlotlyDashStatelessapp(models.Model):
    id = models.BigAutoField(primary_key=True)
    app_name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=110)

    class Meta:
        managed = False
        db_table = 'django_plotly_dash_statelessapp'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EducationBudgets(models.Model):
    gugun = models.ForeignKey('SeoulInfo', models.DO_NOTHING, db_column='gugun')
    detail_code = models.IntegerField(blank=True, null=True)
    budget_amount = models.BigIntegerField(blank=True, null=True)
    code_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'education_budgets'


class HomeNotice(models.Model):
    notice_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    article = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hit = models.PositiveIntegerField()
    author = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'home_notice'


class RealEstate(models.Model):
    building_name = models.CharField(primary_key=True, max_length=50)
    building_address = models.CharField(max_length=50)
    gugun = models.ForeignKey('SeoulInfo', models.DO_NOTHING, db_column='gugun', blank=True, null=True)
    contract_date = models.DateField()
    price = models.IntegerField()
    building_area = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'real_estate'
        unique_together = (('building_name', 'building_address'),)


class SalesCustomers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=64)
    site = models.CharField(max_length=64, blank=True, null=True)
    team = models.CharField(max_length=64, blank=True, null=True)
    position = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=128)
    phone = models.CharField(max_length=11)
    note = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    author = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sales_customers'


class School(models.Model):
    school_id = models.CharField(primary_key=True, max_length=20)
    gugun = models.ForeignKey('SeoulInfo', models.DO_NOTHING, db_column='gugun')
    school_name = models.CharField(max_length=30)
    school_level = models.CharField(max_length=5)
    students_number = models.IntegerField()
    teachers_number = models.IntegerField()
    students_per_class = models.DecimalField(max_digits=3, decimal_places=1)
    school_address = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'school'


class SeoulInfo(models.Model):
    gugun = models.CharField(primary_key=True, max_length=30)
    latitude = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    population = models.IntegerField()
    population_dentisy = models.IntegerField()
    area = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'seoul_info'


class Subway(models.Model):
    subway_station_name = models.CharField(primary_key=True, max_length=50)
    sido = models.CharField(max_length=50)
    gugun = models.ForeignKey(SeoulInfo, models.DO_NOTHING, db_column='gugun')

    class Meta:
        managed = False
        db_table = 'subway'
