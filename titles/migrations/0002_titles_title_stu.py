# Generated by Django 3.1.4 on 2021-01-04 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='titles',
            name='title_stu',
            field=models.CharField(choices=[('SC-1', 'SC-1'), ('SC-2', 'SC-2'), ('SC-3', 'SC-3'), ('COMMERCE', 'COMMERCE'), ('ARTS', 'ARTS')], default='sc1', max_length=10, verbose_name='Class'),
        ),
    ]