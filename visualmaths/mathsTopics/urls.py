from django.urls import path
from . import views

urlpatterns = [
   path('quadratics/', views.quadratics, name='quadratics'),
]