# Mock
from unittest.mock import patch
# Django
from django.test import TestCase
# Local
from artists.models import Artist
from albums.models import Album, Record

""" SetUp the TestCase """

class ArtistModelTestCase(TestCase):
    
    def setUp(self):
        self.album = Album.objects.create(
            name='Random Access Memories',
            creator='Daft Punk',
            slug='random-access-memories'
         )
        self.record = Record.objects.create(
             name='Give Life Back to Music',
             album=self.album,
             record_number=1,
             slug='give-life-back-to-music'
         )
         
        self.artist = Artist.objects.create(
             record=self.record,
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
        
    def test_get_absolute_url(self):
        ''' Test that we can build a URL for a composer '''
        self.assertEqual(
            self.artist.get_abosolute_url(),
            '/recordings/random-access-memories/give-life-back-to-music/daft-punk/')

    @patch('musicbrainzngs.browse_releases')
    @patch('musicbrainzngs.search_artists')
    def test_get_artist_tracks_from_musicbrainz(self, mock_mb_search_artists, mock_mb_browse_releases):
        '''Test that we can make artists from the MusicBrainz API '''
        mock_mb_search_artists.return_value = {
            'artist-list': [
                {
                    'name': 'Maroon 5',
                    'ext:score': '100',
                    'id': '0ab49580-c84f-44d4-875f-d83760ea2cfe',
                    'tag-list': [
                        {'count': '2', 'name': 'pop'},
                        {'count': '1', 'name': 'electropop'}
                    ]
                }
            ]
        }
        
        recording1 = {
            'recording': {
                'id': '6e9889e5-37a2-4081-bf41-dc66665928d8',
                'title': 'Goodnight Goodnight',
            },
            'position': '8'
        
        }
        
        recording2 = {
            'recording': {
                'id': 'e3887c33-9c20-4e10-995a-428cb28e3e91',
                'title': 'Give a little More',
            },
            'position': '2'
        }
        
        mock_mb_browse_releases.return_value = {
            'release-list': [
                {
                    'title': 'It Won\'t Be Soon Before Long',
                    'id': 'cbac27ea-0af2-4340-ba15-7518de4edb9a',
                    'medium-list': [
                        {
                            'track-list': [recording1]
                        }
                    ]
                },
                {
                    'title': 'Hands All Over',
                    'id': 'a659af08-aba4-4fcd-90da-9767e608d47c',
                    'medium-list': [
                        {
                            'track-list': [recording2]
                        }
                    ]
                }
            ]
        }
        
        created_artists = Artist.get_artist_records_from_musicbrainz_api('Maroon 5')
        
        mock_mb_search_artists.assert_called_with('Maroon 5')
        self.assertEqual(len(created_artists), 2)
        self.assertEqual(created_artists[0].artist, 'Maroon 5')
        self.assertEqual(created_artists[1].record.name, 'Goodnight Goodnight')
    
    def test_get_genre_from_musicbrainz_tag_list(self):
        ''' Test that we can map tags from musicbrainz to genres '''
        tag_list = [{'count': '3', 'name': 'electropop'}, {'count': '2', 'name': 'electropop'}, {'count': '2', 'name': 'electropop'}]
        
        self.assertEqual(Artist.get_genre_from_musicbrainz_tag_list(tag_list), 'electropop')
        
        
