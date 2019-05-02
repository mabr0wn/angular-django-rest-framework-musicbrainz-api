# Django rest
from rest_framework import viewsets, mixins
# Local
from artists.models import Artist, Album, Track
from artists.serializers import ArtistSerializer, AlbumSerializer, TrackSerializer


class ArtistViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
   
class TrackViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
        
