from django.db import models

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
    canonical_id = models.ForeignKey(WordCanonical, db_column="canonical_id",on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'word_declension'

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
    nickname = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'
    
class UserSavedWord(models.Model):
    pk_column = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(AuthUser, db_column="user_id", on_delete=models.CASCADE)
    canonical_id = models.ForeignKey('WordCanonical', db_column="canonical_id", on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'user_saved_word'