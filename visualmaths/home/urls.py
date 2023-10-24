from django.urls import path, include
from . import views
import mathsTopics.views

urlpatterns = [
   path('', views.homepage, name='homepage'),
   path('signup/', views.signup, name='signup'),
   path('login/', views.login, name='login'),
   path('dash/', views.dash, name='dash'),
   path('logout/', views.logout, name='logout'),
   path('graph/', views.graph, name='graph'),
   path('subject/', views.subject, name='subject'),
   path('qform/', views.qform, name='qform'),
   path('question/', views.question, name='question'),
   path('quadratics/', mathsTopics.views.quadratics, name='quadratics'),
   path('assessment/', views.weeklyAssessments, name='assess'),
]