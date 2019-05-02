# Django
from django.db import models
from django.template.defaultfilters import slugify
from django.apps import apps
from albums.models import Album, Record
# API
import musicbrainzngs as mb

mb.set_useragent('Mbrown - mattd429@gmail.com', version='0.0.1')

class ArtistManager(models.Manager):

    def get_artist_records_from_musicbrainz_api(self, artist):
        """
        Create album, Record, and artist reords for artists we find
        in the MusicBrainzNGS API
        
        :param artist: an artist's name as a string to search for
        :return: Queryset of artists
        """
        model = apps.get_model('artists', 'Artist')
        search = mb.search_artists(artist)
        results = search['artist-list'][0]
        genre = model.objects.get_genre_from_musicbrainz_tag_list(results['tag-list'])
        
        for album_dict in mb.browse_releases(results['id'], includes=['recordings'])['release-list']:
            album = Album.objects.create(name=album_dict['title'], artist=artist, slug=slugify(album_dict['title']))
            
            """
                Medium-list results from dearch having an additional 
                <track-count> elements containing the number of
                tracks over all mediums.
                e.g. CD 1 of the 1984 US release of "The Wall" by Pink Floyd

            """
            
            for record_dict in album_dict['medium-list'][0]['track-list']:
                record = Record.objects.create(album=album, name=record_dict['recording']['title'],
                                               record_number=record_dict['position'],
                                               slug=slugify(record_dict['recording']['title']))
                artist = model.objects.create(record=record, artist=artist, genre=genre, slug=slugify(artist))
                
            return model.objects.filter(artist=artist)

    def get_genre_from_musicbrainz_tag_list(self, tag_list):
        """
        Return a genre from a list of dict-tags as returned in the
        MusicBrainzNGS API
        
        :param tag_list: a list of dicts with keys 'count' and 'name'
        :return: a string
        """
        map = {'electropop': 'electropop', 'pop': 'pop', 'electronic': 'electronic'}
        return map[set(map.keys()).intersection([tag['name'] for tag in tag_list]).pop()]
