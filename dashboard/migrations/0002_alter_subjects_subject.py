# Generated by Django 3.2 on 2021-05-11 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='subject',
            field=models.CharField(max_length=70),
        ),
    ]
