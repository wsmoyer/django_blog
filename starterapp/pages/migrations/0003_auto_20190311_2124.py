# Generated by Django 2.1.7 on 2019-03-12 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_pages_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='feat_img',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
