# Django
from django.db import models
from django.template.defaultfilters import slugify
from django.apps import apps
from albums.models import Album, Record
# API
import musicbrainzngs as mb


class ArtistManager(models.Manager):

    def music_brainz_artist(self, artist):

        model = apps.get_model('artists', 'Artist')
        search = mb.search_artists(query=artist, limit=1)
        for artist_dict in search['artist-list'][0]:
            artist = model.objects.create(
                                            artist=artist,
                                            slug=slugify(artist)
                                            )   
            artist.save()
            return model.objects.filter(id=artist.id)
        return model.objects.none()   
