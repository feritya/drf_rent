# Generated by Django 4.1.5 on 2023-01-27 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=300, null=True)),
                ('sehir', models.CharField(blank=True, max_length=50, null=True)),
                ('foto', models.FileField(blank=True, null=True, upload_to='profil_fotolari/%Y/%m/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profil', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'profiller',
            },
        ),
        migrations.CreateModel(
            name='ProfilDurum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('durum_mesaji', models.CharField(blank=True, max_length=100, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('güncelleme_zamani', models.DateTimeField(auto_now=True)),
                ('user_profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiller.profil')),
            ],
            options={
                'verbose_name_plural': 'profil mesajlari',
            },
        ),
    ]
