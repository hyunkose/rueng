from django.db import models

class YesasiaArticletitle(models.Model):
    name = 'yesasia'

    article_id = models.AutoField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    is_read = models.IntegerField(blank=True, null=True)
    update_date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yesasia_articletitle'


class YandexArticletitle(models.Model):
    name='yandex_news'

    article_id = models.TextField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    is_read = models.IntegerField(blank=True, null=True)
    update_date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yandex_articletitle'

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

class UserSavedArticle(models.Model):
    pk_column = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(AuthUser, db_column="user_id", on_delete=models.CASCADE)
    article_type = models.TextField(blank=True, null=True)
    yesasia_article_id = models.ForeignKey('YesasiaArticletitle', db_column="yesasia_article_id", related_name = 'yesasia_article_id', on_delete=models.CASCADE, blank=True, null=True)
    yandex_article_id = models.ForeignKey('YandexArticletitle', db_column="yandex_article_id", related_name = 'yandex_article_id', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_saved_article'