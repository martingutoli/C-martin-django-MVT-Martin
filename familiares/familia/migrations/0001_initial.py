# Generated by Django 4.0.6 on 2022-07-31 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datos_familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('fecha_nac', models.DateTimeField()),
                ('edad', models.IntegerField()),
                ('relacion', models.CharField(max_length=40)),
            ],
        ),
    ]
