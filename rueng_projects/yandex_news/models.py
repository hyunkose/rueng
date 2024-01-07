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
