from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView     



class apihomepage(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class detailpage(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "id"

