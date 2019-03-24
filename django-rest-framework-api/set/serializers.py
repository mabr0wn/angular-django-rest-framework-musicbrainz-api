from rest_framework import serializers

from .models import Collection, Record

class seterializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'
        
class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'
