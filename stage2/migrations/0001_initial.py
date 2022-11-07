# Generated by Django 4.1.2 on 2022-11-07 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('operation_type', models.CharField(choices=[('addition', 'addition'), ('subtraction', 'subtraction'), ('multiplication', 'multiplication')], max_length=200)),
            ],
        ),
    ]