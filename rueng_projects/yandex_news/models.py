from django.db import models


class WordCanonical(models.Model):
    name='yandex_news'

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
    name='yandex_news'
    
    declension_id = models.AutoField(primary_key=True)
    form = models.TextField(blank=True, null=True)
    clean_form = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    canonical = models.ForeignKey(WordCanonical, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'word_declension'

class YandexArticlebody(models.Model):
    name='yandex_news'

    contents_id = models.AutoField(primary_key=True)
    contents = models.TextField(blank=True, null=True)
    update_date = models.TextField(blank=True, null=True)
    article_id = models.ForeignKey('YandexArticletitle', models.CASCADE, db_column='article_id')

    class Meta:
        managed = False
        db_table = 'yandex_articlebody'


class YandexArticletitle(models.Model):
    name='yandex_news'

    article_id = models.TextField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    is_read = models.IntegerField(blank=True, null=True)
    update_date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yandex_articletitle'

class SavedVocab(models.Model):
    vocab_id = models.AutoField(primary_key=True, blank=False, null=False)
    canonical_form = models.TextField(blank=True, null=True)
    canonical_id = models.ForeignKey('WordCanonical', models.CASCADE, db_column='canonical_id',blank=True, null=True)
    saved_date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'saved_vocab'

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

class YesasiaArticletitle(models.Model):
    name = 'yesasia'

    article_id = models.AutoField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    is_read = models.IntegerField(blank=True, null=True)
    update_date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yesasia_articletitle'
    
class UserSavedArticle(models.Model):
    pk_column = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(AuthUser, db_column="user_id", on_delete=models.CASCADE)
    article_type = models.TextField(blank=True, null=True)
    yesasia_article_id = models.ForeignKey('YesasiaArticletitle', db_column="yesasia_article_id", related_name = 'yesasia_article_id', on_delete=models.CASCADE, blank=True, null=True)
    yandex_article_id = models.ForeignKey('YandexArticletitle', db_column="yandex_article_id", related_name = 'yandex_article_id', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_saved_article'


class UserSavedWord(models.Model):
    pk_column = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(AuthUser, db_column="user_id", on_delete=models.CASCADE)
    canonical_id = models.ForeignKey('WordCanonical', db_column="canonical_id", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_saved_word'
