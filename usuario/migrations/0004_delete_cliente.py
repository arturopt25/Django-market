# Generated by Django 2.2.1 on 2019-05-14 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_cliente'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]