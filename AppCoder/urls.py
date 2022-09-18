from django.urls import path
from AppCoder.views import *

urlpatterns = [
   path('', index),
   path('cursos/', cursos),
   path('emtregabñes/', entregables),
   path('estudiantes/', estudiantes),
   path('profesores/', profesores)
]
