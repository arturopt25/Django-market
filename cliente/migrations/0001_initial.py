# Generated by Django 2.2.1 on 2019-05-13 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idusuario', models.IntegerField(max_length=50)),
            ],
        ),
    ]
