# Generated by Django 3.2.6 on 2021-08-25 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Nombre'),
        ),
    ]