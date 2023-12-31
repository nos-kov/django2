# Generated by Django 3.2.22 on 2023-11-26 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_remove_article_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='articles', through='articles.Scope', to='articles.Tag'),
        ),
    ]
