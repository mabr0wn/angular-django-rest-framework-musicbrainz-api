# Django rest
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework import filters
from rest_framework.exceptions import NotFound

# Local
from artists.models import Artist, Album, Track
from artists.serializers import ArtistSerializer, AlbumSerializer, TrackSerializer
from .tasks import get_artist_tracks_from_musicbrianz_api


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('artist',  'genre')

    @action(methods=['post'], detail=True)
    def get_queryset(self, **kwargs):
        artists = []

        text = kwargs.get('text', None)
        
        if text:
            artists = Artist.objects.filter(artist=text)

        if not artists:
           artist = get_artist_tracks_from_musicbrianz_api(text)
           artists = [artist]
        return artists

class AlbumViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
   
class TrackViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
        
