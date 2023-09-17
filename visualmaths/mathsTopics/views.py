from django.shortcuts import render
from students.models import Question

# Create your views here.

def quadratics(request):
    return render(request, 'mathsTopics/quadratics.html')

def quadraticsQs(request):
    Question.objects.filter(subject='Maths', topic='Quadratics', difficulty='Easy')