from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import StudentUser

# Create your views here.

def dummy(request):
    template = loader.get_template('students/base.html')
    return HttpResponse(template.render())