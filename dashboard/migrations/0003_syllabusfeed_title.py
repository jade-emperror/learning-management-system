# Generated by Django 3.2 on 2021-05-12 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_subjects_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='syllabusfeed',
            name='title',
            field=models.CharField(default='Differential Calculus', max_length=120),
            preserve_default=False,
        ),
    ]
