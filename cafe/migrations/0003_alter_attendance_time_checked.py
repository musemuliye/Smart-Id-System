# Generated by Django 4.2.4 on 2023-09-07 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0002_attendance_ate_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='time_checked',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
