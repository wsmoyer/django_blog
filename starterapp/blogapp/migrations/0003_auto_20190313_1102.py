# Generated by Django 2.1.7 on 2019-03-13 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_blogpost_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='date published'),
        ),
    ]
