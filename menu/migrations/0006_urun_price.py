# Generated by Django 3.0.7 on 2020-08-17 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_urun_tip'),
    ]

    operations = [
        migrations.AddField(
            model_name='urun',
            name='price',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
