# Generated by Django 2.1.7 on 2019-03-07 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenfapp', '0008_auto_20190307_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recetas',
            name='cantidad_Ing_1',
            field=models.IntegerField(),
        ),
    ]