# Generated by Django 4.1.1 on 2022-12-27 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_slug_news_timing_alter_news_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(max_length=3000),
        ),
    ]
