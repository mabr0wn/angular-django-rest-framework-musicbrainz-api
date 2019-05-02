# Django
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Local
# from albums.models import Album, Record
# Musicbrainz
import musicbrainzngs as mb

class Album(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    slug = models.SlugField()
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name
      
class Record(models.Model):
    name = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    record_number = models.PositiveIntegerField(blank=True, null=True)
    slug = models.SlugField()

class Artist(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    artist = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    start_time = models.CharField(max_length=20, blank=True, null=True)
    end_time = models.CharField(max_length=20, blank=True, null=True)
    slug = models.SlugField()
    
    class Meta:
        ordering = ['record', 'start_time']
    
    def get_absolute_url(self):
        return reverse('artist_detail_view', kwargs={'album': self.record.album.slug, 'record': self.record.slug,
                                                       'artist': self.slug})
    def get_period_of_play_time(self):
        play_string = ''
        if self.start_time and self.end_time:
            play_string = '{}-{}'.format(self.start_time, self.end_time)
        return play_string
    ''' From MusicBrainzNGS '''
    @classmethod
    def get_artist_records_from_musicbrainz_api(cls, artist):
        """
        Create album, Record, and artist reords for artists we find
        in the MusicBrainzNGS API
        
        :param artist: an artist's name as a string to search for
        :return: Queryset of artists
        """
        search = mb.search_artists(artist)
        results = search['artist-list'][0]
        genre = Artist.get_genre_from_musicbrainz_tag_list(results['tag-list'])
        
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
                Artist.objects.create(record=record, artist=artist, genre=genre, slug=slugify(artist))
                
            return Artist.objects.filter(artist=artist)
    @classmethod
    def get_genre_from_musicbrainz_tag_list(cls, tag_list):
        """
        Return a genre from a list of dict-tags as returned in the
        MusicBrainzNGS API
        
        :param tag_list: a list of dicts with keys 'count' and 'name'
        :return: a string
        """
        map = {'electropop': 'electropop', 'pop': 'pop', 'electronic': 'electronic'}
        return map[set(map.keys()).intersection([tag['name'] for tag in tag_list]).pop()]
