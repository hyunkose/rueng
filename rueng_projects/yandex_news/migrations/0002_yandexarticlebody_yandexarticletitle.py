# Generated by Django 4.2.7 on 2023-12-20 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yandex_news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='YandexArticlebody',
            fields=[
                ('contents_id', models.AutoField(primary_key=True, serialize=False)),
                ('contents', models.TextField(blank=True, null=True)),
                ('update_date', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'yandex_articlebody',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='YandexArticletitle',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('is_read', models.IntegerField(blank=True, null=True)),
                ('update_date', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'yandex_articletitle',
                'managed': False,
            },
        ),
    ]
