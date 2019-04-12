# Mock
from unittest.mock import patch, Mock
# Django
from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
# Local
from artists.views import index, artist_detail
from artists.models import Artist
from albums.models import Album, Record

class ArtistBaseTestCase(TestCase):
    
    def setUp(self):
        # Returns a request
        self.factory = RequestFactory()
        
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.voices = Album.objects.create(name='Voices', slug='voices')
        cls.nothing_but_trouble = Record.objects.create(name='Nothing but Trouble', slug='nothing-but-trouble', album=cls.voices)
        cls.electropop_artist = Artist.objects.create(genre='electropop', creator='Phantogram', record=cls.nothing_but_trouble,
                                                              slug='phantogram')
        cls.permanent_signal = Album.objects.create(name='Permanent Signal', slug='permanent-signal')
        cls.the_way_out = Record.objects.create(name='The Way Out', slug='the-way-out', album=cls.permanent_signal)
        cls.dream_pop_artist = Artist.objects.create(genre='dream pop', creator='Procelain Raft', record=cls.the_way_out,
                                                             slug='procelain-raft')
            
class IndexViewTestCase(ArtistBaseTestCase):
    
    def test_index_view_basic(self):
        ''' Test that the index view returns a 200 response uses the correct template '''
        request = self.factory.get('/')
        response - index(request)
        with self.assertTemplateUsed('artists/index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)
    
    def test_index_view_returns_artist(self):
        ''' Test that the index will attempt to return artist if query parameters exist '''
        
        # Client will return a response
        response = self.client.get('/', {'genre': 'electropop'})
        artists = response.context['artists']
        
        self.assertEqual(type(artists), QuerySet)
        self.assertEqual(len(artists), 1)
        self.assertEqual(artists[0].creator, 'Phantogram')
    
    @patch('artists.models.artist.get_artist_tracks_from_musicbrainz_api')
    def test_index_view_returns_external_tracks(self, mock_artists_get_from_mb):
        ''' Test that the index view will return artists from the MusicBrainz API if none are returned'''
        mock_muscian = Mock()
        mock_artist.creator = 'Maroon 5'
        mock_artist_get_from_mb.return_value = [mock_artist]
        
        response = self.client.get('/', {
            'genre': 'pop',
            'creator': 'Maroon 5' # Not in DB
        })
        
        artists = response.context['artists']
        self.assertEqual(len(artists), 1)
        self.assertEqual(artists[0].creator, 'Maroon 5')

class ArtistViewTestCase(ArtistBaseTestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
    
    def test_basic(self):
        self.factory = RequestFactory()
        
    def test_basic(self):
        ''' Test that artist view returns a 200 response, uses the correct template, and has the correct context '''
        request = self.factory.get('/artists/voices/nothing-but-trouble/phantogram/')
        
        with self.assertTemplateUsed('artists/artist_detail.html'):
            response = artist_detail(request, album=self.voices.slug, record=self.nothing_but_trouble.slug,
                                       creator=self.electropop_artist.slug)
            self.assertEqual(response.status_code, 200)
            page = response.content.decode()
            self.assertInHTML('<p id="mb-artist">Phantogram</p>', page)
            self.assertInHTML('<p id="mb-track">Nothing but Trouble [1 composer]', page)
