# Generated by Django 2.1.7 on 2019-04-07 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('greenfapp', '0002_auto_20190406_2221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cantidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Cantidad',
            },
        ),
        migrations.AlterField(
            model_name='ingredientes',
            name='cantidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='greenfapp.Cantidad'),
        ),
    ]