# Generated by Django 2.2.5 on 2019-09-16 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Final', '0003_auto_20190916_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagen',
            name='cadena1',
            field=models.CharField(default='', editable=False, max_length=1000),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='cadena',
            field=models.CharField(default='', editable=False, max_length=10000),
        ),
    ]
