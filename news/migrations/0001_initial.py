# Generated by Django 4.1.1 on 2022-12-15 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbercard', models.CharField(max_length=2)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=3000)),
                ('image', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('date', models.DateTimeField(null=True)),
            ],
        ),
    ]
