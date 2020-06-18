from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import polices
from . serializers import policesSerializer

# Create your views here.

class police(APIView):  # inherits from an APIView
	
	def get(self, request):
		obj = polices.objects.all()   # creating objects of all the values
		serializer = policesSerializer(obj, many=True)  # pass these objects to the serializer which will convert them to json
		return Response(serializer.data, status=200)

	def post(self, request):
		data = request.data
		serializer = policesSerializer(data=data)  # this means that our data is being assigned to the data object, and hence a post request
		if serializer.is_valid():
			serializer.save()  # to do post request
			return Response(serializer.data, status=201)
		return Response(serializer.errors, status=400)


class policebyid(APIView):  # inherits from an APIView
	
	def get_object(self, id):
		try:
			return polices.objects.get(id=id)
		except polices.DoesNotExist as e:
			return Response({"error": "Given police record not found."}, status=404)

	def get(self, request, id=None):  # automatically detected what we specify as slash
		instance = self.get_object(id)   # Getting the object of the specified id
		serializer = policesSerializer(instance)  # pass these objects to the serializer which will convert them to json
		return Response(serializer.data)

	def put(self, request, id=None):
		data = request.data  # Our requested data which will be overwritten to the id we specify
		instance = self.get_object(id)   # Getting the object of the specified id
		serializer = policesSerializer(instance, data=data)  # instance is passed which contains our present data at that particular ID. This will be overwriten by our new data.
		if serializer.is_valid():
			serializer.save()  # to do post request
			return Response(serializer.data, status=200)
		return Response(serializer.errors, status=400)

	def delete(self, request, id=None):
		instance = self.get_object(id)
		serializer = policesSerializer(instance)  # pass these objects to the serializer which will convert them to json
		instance.delete()
		return Response(serializer.data)
