from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import alerts
from . serializers import alertsSerializer

# Create your views here.

class alert(APIView):  # inherits from an APIView
	
	def get(self, request):
		obj = alerts.objects.all()   # creating objects of all the values
		serializer = alertsSerializer(obj, many=True)  # pass these objects to the serializer which will convert them to json
		return Response(serializer.data)

	def post(self):
		pass

