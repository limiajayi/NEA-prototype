# Generated by Django 4.2.4 on 2023-09-24 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_mathspoints_furthermathspoints'),
    ]

    operations = [
        migrations.AddField(
            model_name='furthermathspoints',
            name='volumes_of_revolution',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
