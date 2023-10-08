from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class StudentUser(models.Model):
    username = models.CharField(max_length=50, null=True, unique=True)
    password = models.CharField(max_length=250, null=True)
    maths = models.BooleanField(default=1, null=True)
    further_maths = models.BooleanField(null=True)

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
      self.password = make_password(self.password)
      super(StudentUser, self).save(*args, **kwargs)
    
Q_CHOICES = [
   ("Easy", "Easy"),
   ("Medium", "Medium"),
   ("Hard", "Hard"),
]

SUBJECT_CHOICES = [
   ("Maths", "Maths"),
   ("Further Maths", "Further Maths")
]


TOPIC_CHOICES = [
   ("Quadratics", "Quadratics"),
   ("Equations and Inequalities", "Equations and Inequalities"),
   ("Graphs and Transformations", "Graphs and Transformations"),
   ("Straight Line Graphs", "Straight Line Graphs"),
   ("Circles", "Circles"),
   ("Trigonometry", "Trigonometry"),
   ("Differentiation", "Differentiation"),
   ("Integration", "Integration"),
   ("Exponentials and Logarithms", "Exponentials and Logarithms"),
   ("2D Vectors", "2D Vectors"),
   ("Argand Diagrams", "Argand Diagrams"),
   ("Volumes of Revolution", "Volumes of Revolution"),
   ("Methods In Calculus", "Methods In Calculus"),
   ("Matrices", "Matrices"),
   ("3D Vectors", "3D Vectors"),
   ("Polar Coordinates", "Polar Coordinates"),
   ("Hyperbolic Functions", "Hyperbolic Functions"),
]
        

class Question(models.Model):
   question = models.CharField(max_length=500, null=True)
   answer = models.CharField(max_length=1000, null=True)
   subject = models.CharField(max_length=30, null=True, choices=SUBJECT_CHOICES)
   topic = models.CharField(max_length=100, null=True, blank=True, choices=TOPIC_CHOICES)
   difficulty = models.CharField(max_length=10, null=True, choices=Q_CHOICES)
   image = models.ImageField(upload_to='questions/', null=True, blank=True)
   mark_scheme = models.ImageField(upload_to='markschemes/', null=True, blank=True)
   answer_box = models.IntegerField(null=True, blank=True)

   def __str__(self):
        return self.question
   
class MathsPoints(models.Model):
    username = models.OneToOneField(StudentUser, on_delete=models.CASCADE, null=True, unique=True)
    quadratics = models.IntegerField(default=0, blank=True)
    equations_and_inequalities = models.IntegerField(default=0, blank=True)
    graphs_and_transformations = models.IntegerField(default=0, blank=True)
    straight_line_graphs = models.IntegerField(default=0, blank=True)
    circles = models.IntegerField(default=0, blank=True)
    trigonometry = models.IntegerField(default=0, blank=True)
    differentiation = models.IntegerField(default=0, blank=True)
    integration = models.IntegerField(default=0, blank=True)
    two_d_vectors = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return str(self.username)
    
class FurtherMathsPoints(models.Model):
    username = models.OneToOneField(StudentUser, on_delete=models.CASCADE, null=True, unique=True)
    differentiation = models.IntegerField(default=0, blank=True)
    integration = models.IntegerField(default=0, blank=True)
    argand_diagrams = models.IntegerField(default=0, blank=True)
    volumes_of_revolution = models.IntegerField(default=0, blank=True)
    methods_in_calculus = models.IntegerField(default=0, blank=True)
    matrices = models.IntegerField(default=0, blank=True)
    polar_coordinates = models.IntegerField(default=0, blank=True)
    hyperbolic_functions = models.IntegerField(default=0, blank=True)
    three_d_vectors = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return str(self.username)
    
    def findField(self, word):
        return self.word

    
