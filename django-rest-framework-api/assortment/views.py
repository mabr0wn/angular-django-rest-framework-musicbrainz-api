from rest_framework import viewsets, mixins

from .models import Assortment, Record
from .serializers import AssortmentSerializer, RecordSerializer

class CollectionViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Assortment.objects.all()
    serializer_class = AssortmentSerializer
   
class RecordViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
