from unittest.mock import patch, Mock

from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet

from experiments.views import index, musician_detail
from experiments.models import Musician
from collections.models import Collection, Record

class MusicianBaseTestCase(TestCase):
    
    def setUp(self):
        # Returns a request
        self.factory = RequestFactory()
        
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.voices = Collection.objects.create(name='Voices', slug='voices')
        cls.nothing_but_trouble = Record.objects.create(name='Nothing but Trouble', slug='nothing-but-trouble', collection=cls.voices)
        cls.electropop_musician = Musician.objects.create(genre='electropop', creator='Phantogram', record=cls.nothing_but_trouble,
                                                              slug='phantogram')
        cls.permanent_signal = Collection.objects.create(name='Permanent Signal', slug='permanent-signal')
        cls.the_way_out = Record.objects.create(name='The Way Out', slug='the-way-out', collection=cls.permanent_signal)
        cls.dream_pop_musician = Musician.objects.create(genre='dream pop', creator='Procelain Raft', record=cls.the_way_out,
                                                             slug='procelain-raft')
            
class IndexViewTestCase(MusicianBaseTestCase):
    
    def test_index_view_basic(self):
        ''' Test that the index view returns a 200 response uses the correct template '''
        request = self.factory.get('/')
        response - index(request)
        with self.assertTemplateUsed('musicians/index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)
    
    def test_index_view_returns_musician(self):
        ''' Test that the index will attempt to return Musician if query parameters exist '''
        
        # Client will return a response
        response = self.client.get('/', {'genre': 'electropop'})
        musicians = response.context['musicians']
        
        self.assertEqual(type(musicians), QuerySet)
        self.assertEqual(len(musicians), 1)
        self.assertEqual(musicians[0].creator, 'Phantogram')
    
    @patch('experiments.models.Musician.get_artist_tracks_from_musicbrainz_api')
    def test_index_view_returns_external_tracks(self, mock_musicians_get_from_mb):
        ''' Test that the index view will return artists from the MusicBrainz API if none are returned'''
        mock_muscian = Mock()
        mock_musician.creator = 'Maroon 5'
        mock_musician_get_from_mb.return_value = [mock_musician]
        
        response = self.client.get('/', {
            'genre': 'pop',
            'creator': 'Maroon 5' # Not in DB
        })
        
        musicians = response.context['musicians']
        self.assertEqual(len(musicians), 1)
        self.assertEqual(musicians[0].creator, 'Maroon 5')
