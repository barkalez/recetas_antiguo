# Generated by Django 2.1.7 on 2019-03-07 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenfapp', '0004_auto_20190307_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recetas',
            name='ingrediente_2',
            field=models.TextField(blank=True, null=True),
        ),
    ]