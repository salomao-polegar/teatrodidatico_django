from django.urls import path, include
from .views import *
from django.conf import settings

urlpatterns = [
    path('', index, name="index"),
    path('index', index, name="index"),
    path('cursos/<int:curso_id>', cursos, name="cursos")
]

