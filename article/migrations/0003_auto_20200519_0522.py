# Generated by Django 2.1.5 on 2020-05-19 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20200519_0444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Makalenize Fotoğraf Ekleyin (isteğe bağlı)'),
        ),
    ]
