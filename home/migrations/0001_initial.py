# Generated by Django 3.0.7 on 2020-08-16 11:06

import ckeditor_uploader.fields
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
            name='Ayarlar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(blank=True, max_length=150)),
                ('anahtar_kelime', models.CharField(blank=True, max_length=250)),
                ('company', models.CharField(blank=True, max_length=50)),
                ('adress', models.CharField(blank=True, max_length=150)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('phone_2', models.CharField(blank=True, max_length=20)),
                ('fax', models.CharField(blank=True, max_length=15)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('smtpserver', models.CharField(blank=True, max_length=20)),
                ('smtpemail', models.CharField(blank=True, max_length=20)),
                ('smtp_password', models.CharField(blank=True, max_length=15)),
                ('smtp_port', models.CharField(blank=True, max_length=5)),
                ('icon', models.ImageField(blank=True, upload_to='images/')),
                ('logo', models.ImageField(blank=True, upload_to='images/')),
                ('facebook', models.CharField(blank=True, max_length=255)),
                ('twitter', models.CharField(blank=True, max_length=50)),
                ('instagram', models.CharField(blank=True, max_length=50)),
                ('hakkimizda', ckeditor_uploader.fields.RichTextUploadingField()),
                ('iletisim', ckeditor_uploader.fields.RichTextUploadingField()),
                ('referanslar', ckeditor_uploader.fields.RichTextUploadingField()),
                ('status', models.CharField(blank=True, choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactFormMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('subject', models.CharField(blank=True, max_length=50)),
                ('message', models.CharField(blank=True, max_length=250)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('note', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(blank=True, choices=[('New', 'Yeni'), ('Read', 'Okundu'), ('Closed', 'Cevaplandi')], default='New', max_length=20)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordernumber', models.IntegerField()),
                ('question', models.CharField(blank=True, max_length=250)),
                ('answer', models.TextField(blank=True)),
                ('status', models.CharField(blank=True, choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('adress', models.CharField(blank=True, max_length=150)),
                ('image', models.ImageField(blank=True, upload_to='images/users')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
