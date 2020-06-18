from rest_framework import serializers
from . models import zones

class zonesSerializer(serializers.ModelSerializer):

	class Meta:
		model = zones
		fields = '__all__'