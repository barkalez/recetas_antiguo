# Generated by Django 2.1.7 on 2019-03-08 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('greenfapp', '0017_auto_20190308_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='recetas',
            name='cantidad_Ing_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recetas',
            name='ingrediente_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recetas_requests_created4a', to='greenfapp.Ingredientes'),
        ),
        migrations.AddField(
            model_name='recetas',
            name='tipo_Cant_Ing_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recetas_requests_created4b', to='greenfapp.TipCant'),
        ),
    ]