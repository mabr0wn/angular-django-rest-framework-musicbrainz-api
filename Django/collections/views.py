from rest_framework import viewsets, mixins

from .models import Collection, Record
from .serializers import CollectionSerializer, RecordSerializer

class CollectionViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Collection.objects.all()
    serializer_class = CollecionSerializer
   
class RecordViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
