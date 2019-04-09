# Django rest
from rest_framework import viewsets, mixins
# Local
from .models import Assortment, Record
from .serializers import AssortmentSerializer, RecordSerializer

class AssortmentViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Assortment.objects.all()
    serializer_class = AssortmentSerializer
   
class RecordViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
