# Generated by Django 2.1.7 on 2019-03-07 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('greenfapp', '0002_auto_20190307_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recetas',
            name='ingrediente_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='greenfapp.Ingredientes'),
        ),
    ]
