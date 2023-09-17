from django.shortcuts import render

# Create your views here.

def quadratics(request):
    return render(request, 'mathsTopics/quadratics.html')