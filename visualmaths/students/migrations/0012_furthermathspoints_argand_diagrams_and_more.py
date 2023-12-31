# Generated by Django 4.2.4 on 2023-10-08 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0011_alter_furthermathspoints_differentiation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='furthermathspoints',
            name='argand_diagrams',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='furthermathspoints',
            name='three_d_vectors',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='mathspoints',
            name='two_d_vectors',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='topic',
            field=models.CharField(blank=True, choices=[('Quadratics', 'Quadratics'), ('Equations and Inequalities', 'Equations and Inequalities'), ('Graphs and Transformations', 'Graphs and Transformations'), ('Straight Line Graphs', 'Straight Line Graphs'), ('Circles', 'Circles'), ('Trigonometry', 'Trigonometry'), ('Differentiation', 'Differentiation'), ('Integration', 'Integration'), ('Exponentials and Logarithms', 'Exponentials and Logarithms'), ('2D Vectors', '2D Vectors'), ('Argand Diagrams', 'Argand Diagrams'), ('Volumes of Revolution', 'Volumes of Revolution'), ('Methods In Calculus', 'Methods In Calculus'), ('Matrices', 'Matrices'), ('3D Vectors', '3D Vectors'), ('Polar Coordinates', 'Polar Coordinates'), ('Hyperbolic Functions', 'Hyperbolic Functions')], max_length=100, null=True),
        ),
    ]
