from rest_framework import serializers
from . models import polices

class policesSerializer(serializers.ModelSerializer):

	class Meta:
		model = polices
		fields = '__all__'