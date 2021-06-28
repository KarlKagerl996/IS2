# Generated by Django 2.2.6 on 2019-11-01 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('LineaBase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('prioridad', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=200)),
                ('version', models.CharField(max_length=200)),
                ('id_lb', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='LineaBase.LineaBase')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'items',
            },
        ),
    ]
