# Generated by Django 4.2.4 on 2023-09-15 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_alter_question_image_alter_question_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='questions/'),
        ),
        migrations.AlterField(
            model_name='question',
            name='mark_scheme',
            field=models.ImageField(blank=True, null=True, upload_to='markschemes/'),
        ),
    ]