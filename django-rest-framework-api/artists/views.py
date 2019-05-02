# Django
from django.views.generic import TemplateView
# Django rest
from rest_framework import viewsets, mixins
# Local
from artists.models import Artist
from artists.serializers import ArtistSerializer
# Musicbrainz
import musicbrainzngs as mb


class ArtistViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
        
