# Generated by Django 4.1.5 on 2023-01-27 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='roll_number',
            field=models.IntegerField(),
        ),
    ]
