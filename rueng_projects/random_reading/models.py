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