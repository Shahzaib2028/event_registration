# Generated by Django 4.1.1 on 2022-09-10 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_mobile_number'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile_number',
            field=models.CharField(default='', max_length=11, unique=True),
        ),
    ]
