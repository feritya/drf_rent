# Generated by Django 4.1.5 on 2023-02-03 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arac', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carreservation',
            old_name='totoal_price',
            new_name='total_price',
        ),
    ]
