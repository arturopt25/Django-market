# Generated by Django 2.2.1 on 2019-05-14 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idproducto', models.IntegerField(default=170)),
                ('numero_De_item', models.IntegerField(default=170)),
                ('precio_total', models.FloatField(default=170)),
            ],
        ),
    ]
