# Generated by Django 2.2.5 on 2019-09-05 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Final', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='cadena',
            field=models.ImageField(upload_to='Imagens'),
        ),
    ]
