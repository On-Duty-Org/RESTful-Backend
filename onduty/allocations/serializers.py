from rest_framework import serializers
from . models import allocations

class allocationsSerializer(serializers.ModelSerializer):
	zone_name= serializers.ReadOnlyField(source='zone.name')        # To ensure that we get names instead of id's while taking foreign key
	police_name= serializers.ReadOnlyField(source='police.name')


	class Meta:
		model = allocations
		fields = ('id', 'zone_name', 'police_name', 'date_posted', 'time', 'date')