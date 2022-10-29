# Generated by Django 4.1.2 on 2022-10-29 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SlackUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True, verbose_name='Slack Username')),
                ('backend', models.BooleanField(default=False)),
                ('age', models.IntegerField()),
                ('bio', models.TextField()),
            ],
        ),
    ]