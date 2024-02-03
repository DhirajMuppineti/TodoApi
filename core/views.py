from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *

from rest_framework import permissions
from rest_framework import viewsets



class BlogViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.AllowAny]
