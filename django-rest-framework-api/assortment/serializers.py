# Django rest
from rest_framework import serializers
# Local
from .models import Assortment, Record

class AssortmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assortment
        fields = '__all__'
        
class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'
