# Django rest
from rest_framework import viewsets, mixins
# Local
from artists.models import Artist, Album, Record
from artists.serializers import ArtistSerializer, AlbumSerializer, RecordSerializer


class ArtistViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
   
class RecordViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
        
