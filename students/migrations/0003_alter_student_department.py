# Generated by Django 4.2.5 on 2023-09-28 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0002_alter_campus_options'),
        ('students', '0002_alter_disciplinaryrecord_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='students', to='campuses.department'),
        ),
    ]
