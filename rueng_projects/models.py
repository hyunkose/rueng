# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

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


class SavedVocab(models.Model):
    vocab_id = models.AutoField(primary_key=True, blank=False, null=False)
    canonical_form = models.TextField(blank=True, null=True)
    canonical_id = models.ForeignKey('WordCanonical', models.CASCADE, db_column='canonical_id',blank=True, null=True)
    saved_date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'saved_vocab'


class WordCanonical(models.Model):
    canonical_id = models.AutoField(primary_key=True)
    canonical_form = models.TextField(blank=True, null=True)
    pos = models.TextField(blank=True, null=True)
    meaning = models.TextField(blank=True, null=True)
    verb_aspect = models.TextField(blank=True, null=True)
    imperfective_perfective = models.TextField(blank=True, null=True)
    is_saved = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'word_canonical'


class WordDeclension(models.Model):
    declension_id = models.AutoField(primary_key=True)
    form = models.TextField(blank=True, null=True)
    clean_form = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    canonical_id = models.ForeignKey(WordCanonical, models.CASCADE, db_column='canonical_id')

    class Meta:
        managed = False
        db_table = 'word_declension'


class YesasiaArticlebody(models.Model):
    contents_id = models.AutoField(primary_key=True)
    contents = models.TextField(blank=True, null=True)
    update_date = models.TextField(blank=True, null=True)
    article_id = models.ForeignKey('YesasiaArticletitle', models.CASCADE, db_column='article_id')

    class Meta:
        managed = False
        db_table = 'yesasia_articlebody'


class YesasiaArticletitle(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    is_read = models.IntegerField(blank=True, null=True)
    update_date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yesasia_articletitle'
