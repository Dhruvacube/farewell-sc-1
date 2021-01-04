# Generated by Django 3.1.4 on 2021-01-04 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_entry', models.TextField(verbose_name='The about us on the entry page')),
                ('title_limit', models.IntegerField(default=5, verbose_name='No of times a one a vote for a particular title  per day')),
                ('nickname_limit', models.IntegerField(default=20, verbose_name='No of times a one a give nicknames per day')),
                ('vote_nicknameassigntime', models.DateTimeField(verbose_name='Time limit of assigning votes and nickname')),
            ],
        ),
    ]
