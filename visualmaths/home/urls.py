from django.urls import path
from . import views

urlpatterns = [
   path('', views.homepage, name='homepage'),
   path('signup/', views.signup, name='signup'),
   path('login/', views.login, name='login'),
   path('dash/', views.dash, name='dash'),
   path('logout/', views.logout, name='logout'),
   path('graph/', views.graph, name='graph'),
   path('qform/', views.qform, name='qform'),
   path('question/', views.question, name='question'),
]