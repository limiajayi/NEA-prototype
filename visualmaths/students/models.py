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
   ("EASY", "Easy"),
   ("MEDIUM", "Medium"),
   ("HARD", "Hard"),
]

SUBJECT_CHOICES = [
   ("MATHS", "Maths"),
   ("FURTHER MATHS", "Further Maths")
]


TOPIC_CHOICES = [
   ("QUADRATICS", "Quadratics"),
   ("EQUATIONS AND INEQUALITIES", "Equations and Inequalities"),
   ("GRAPHS AND TRANSFORMATIONS", "Graphs and Transformations"),
   ("STRAIGHT LINE GRAPHS", "Straight Line Graphs"),
   ("CIRCLES", "Circles"),
   ("TRIGONOMETRY", "Trigonometry"),
   ("DIFFERENTIATION", "Differentiation"),
   ("INTEGRATION", "Integration"),
   ("EXPONENTIALS AND LOGARITHMS", "Exponentials and Logarithms"),
   ("2DVECTORS", "2D Vectors"),
   ("ARGAND DIAGRAMS", "Argand Diagrams"),
   ("VOLUMES OF REVOLUTION", "Volumes of Revolution"),
   ("METHODS IN CALCULUS", "Methods in Calculus"),
   ("MATRICES", "Matrices"),
   ("3DVECTORS", "3D Vectors"),
   ("POLAR COORDINATES", "Polar Coordinates"),
   ("HYPERBOLIC FUNCTIONS", "Hyperbolic functions"),
]
        

class Question(models.Model):
   question = models.CharField(max_length=500, null=True)
   answer = models.CharField(max_length=50, null=True)
   subject = models.CharField(max_length=30, null=True, choices=SUBJECT_CHOICES)
   topic = models.CharField(max_length=100, null=True, blank=True, choices=TOPIC_CHOICES)
   difficulty = models.CharField(max_length=10, null=True, choices=Q_CHOICES)
   image = models.ImageField(upload_to='questions/', null=True, blank=True)
   mark_scheme = models.ImageField(upload_to='markschemes/', null=True, blank=True)
   answer_box = models.IntegerField(null=True, blank=True)

   def __str__(self):
        return self.question
    
