from django.test import TestCase
from django.core.urlresolvers import resolve

from experiments.views import index

class ExperimentURLsTestCase(TestCase):
    
    def test_root_url_uses_index_view(self):
       ''' Test that the root of the site resolves to the correct view function '''
        root = resolve('/')
        self.assertEqual(root.func, index)
        
    def test_musician_details_url(self):
        ''' Test that the URL for MusicianDetail resolves to the correct view function '''
        musician_detial = resolve('/recordings/lemonade/hold-up/beyoncé/')
        
        self.assertEqual(musician_detail.func.__name__, 'musician_detail')
        self.assertEqual(musician_detail.kwargs['collection'], 'lemonade')
        self.assertEqual(musician_detail.kwargs['record'], 'hold-up')
        self.assertEqual(musician_detail.kwargs['creator'], 'beyoncé')
