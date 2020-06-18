from rest_framework import serializers
from . models import alerts

class alertsSerializer(serializers.ModelSerializer):

	class Meta:
		model = alerts
		fields = '__all__'