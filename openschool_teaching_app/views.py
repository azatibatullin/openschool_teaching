from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from .models import Discipline
from .serializers import DisciplineSerializer

class DisciplineViewSet(viewsets.ModelViewSet):
    queryset = Discipline.objects.all().order_by('-name')
    serializer_class = DisciplineSerializer