# Generated by Django 2.2.6 on 2019-11-02 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0004_auto_20191029_1237'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='proyecto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='proyectos.Proyecto'),
        ),
    ]