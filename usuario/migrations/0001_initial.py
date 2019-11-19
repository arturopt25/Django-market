# Generated by Django 2.2.1 on 2019-05-13 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('email', models.CharField(max_length=120)),
                ('telefono', models.IntegerField(default=170)),
                ('contraseña', models.CharField(max_length=50)),
            ],
        ),
    ]