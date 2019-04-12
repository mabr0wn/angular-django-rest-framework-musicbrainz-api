# Django rest
from rest_framework import viewsets, mixins
# Local
from .models import Album, Record
from .serializers import AlbumSerializer, RecordSerializer

class AlbumViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
   
class RecordViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
