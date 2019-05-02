# Django
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Musicbrainz
import musicbrainzngs as mb

class Album(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    image = models.URLField(blank=True, default='')
    slug = models.SlugField()
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name
      
class Track(models.Model):
    name = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    track_number = models.PositiveIntegerField(blank=True, null=True)
    slug = models.SlugField()

class Artist(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    artist = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    start_time = models.CharField(max_length=20, blank=True, null=True)
    end_time = models.CharField(max_length=20, blank=True, null=True)
    slug = models.SlugField()
    
    class Meta:
        ordering = ['track', 'start_time']
    
    def get_period_of_play_time(self):
        play_string = ''
        if self.start_time and self.end_time:
            play_string = '{0}-{1}'.format(self.start_time, self.end_time)
        return play_string
    
    @classmethod
    def get_genre_from_musicbrainz_tag_list(cls, tag_list):
        """
        Return a genre from a list of dict-tags as returned in the
        MusicBrainzNGS API
        
        :param tag_list: a list of dicts with keys 'count' and 'name'
        :return: a string
        """
        map = {
            'electro': 'electropop',
            'pop': 'pop',
            'electron': 'electronic'
        }
        try:
            return map[set(map.keys()).intersection([tag['name'] for tag in tag_list]).pop()]
        except KeyError:
            return 'unknown'

            

