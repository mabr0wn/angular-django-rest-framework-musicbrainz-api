# Django
from django.test import TestCase
from django.urls import resolve
# Local
from artists.views import Index

class ExperimentURLsTestCase(TestCase):
    
    def test_root_url_uses_index_view(self):
       ''' Test that the root of the site resolves to the correct view function '''
       root = resolve('/')
       self.assertEqual(root.func, Index)
