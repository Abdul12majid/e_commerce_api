from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from hackathon.models import Product
from .serializers import ProductSerializer, Product_Serializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

class ApiProducts(ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


#class Apiproduct(RetrieveUpdateDestroyAPIView):
#	queryset = Product.objects.all()
#	serializer_class = ProductSerializer

