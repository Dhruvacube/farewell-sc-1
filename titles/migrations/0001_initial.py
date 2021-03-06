# Generated by Django 3.1.5 on 2021-01-15 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_name', models.CharField(blank=True, max_length=250, null=True, unique=True, verbose_name='Title Name')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Description of the Title')),
                ('gender', models.CharField(choices=[('ALL', 'ALL'), ('m', 'Male'), ('f', 'Female')], default='m', max_length=6, verbose_name='Gender')),
                ('title_stu', models.CharField(choices=[('ALL', 'ALL'), ('SC-1', 'SC-1'), ('SC-2', 'SC-2'), ('SC-3', 'SC-3'), ('COMMERCE', 'COMMERCE'), ('ARTS', 'ARTS')], default='sc1', max_length=10, verbose_name='Class')),
                ('slug', models.CharField(blank=True, max_length=250, null=True, unique=True, verbose_name='Slug of the Title')),
                ('total_vote', models.PositiveBigIntegerField(default=0, verbose_name='Total No of Vote Registered')),
            ],
            options={
                'verbose_name_plural': 'Titles',
                'ordering': ('-total_vote', 'title_name'),
            },
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_vote', models.PositiveBigIntegerField(default=0, verbose_name='Total No of Vote Registered by this student for the event')),
                ('student', models.ForeignKey(limit_choices_to=models.Q(hidden=False), on_delete=django.db.models.deletion.CASCADE, to='student.student', verbose_name='Student Model')),
                ('title_part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='titles.titles', verbose_name='Titles Model')),
            ],
            options={
                'verbose_name_plural': 'Participants',
                'ordering': ('-stu_vote', 'title_part'),
            },
        ),
    ]
