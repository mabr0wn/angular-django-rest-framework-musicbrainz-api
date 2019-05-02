# Mock
from unittest.mock import patch
# Django
from django.test import TestCase
# Local
from artists.models import Artist, Album, Track

class ArtistModelTestCase(TestCase):
    
    def setUp(self):
        self.album = Album.objects.create(
            name='Random Access Memories',
            artist='Daft Punk',
            slug='random-access-memories'
         )
        self.track = Track.objects.create(
             name='Give Life Back to Music',
             album=self.album,
             track_number=1,
             slug='give-life-back-to-music'
         )
         
        self.artist = Artist.objects.create(
             track=self.track,
             artist='Daft Punk',
             genre='electronic',
             start_time='0:16',
             end_time='4:34',
             slug='daft-punk'
         )

    def test_artist_basic(self):
        ''' Test the basic functionality of artist '''
        self.assertEqual(self.artist.artist, 'Daft Punk'),
        self.assertEqual(self.artist.end_time, '4:34')
    
    def test_get_duration(self):
        """
        Test that we can print the duration of a Artist
        """
        self.assertEqual(self.artist.get_period_of_play_time(), '0:16-4:34')
        
    def test_get_genre_from_musicbrainz_tag_list(self):
        ''' Test that we can map tags from musicbrainz to genres '''
        tag_list = [{'count': '3', 'name': 'electro'}]
        
        self.assertEqual(Artist.get_genre_from_musicbrainz_tag_list(tag_list), 'electropop')
        
        
