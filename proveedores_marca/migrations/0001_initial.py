# Generated by Django 2.2.1 on 2019-05-14 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedores_Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa_marca', models.CharField(max_length=70)),
                ('idproveedores', models.IntegerField(default=170)),
            ],
        ),
    ]
