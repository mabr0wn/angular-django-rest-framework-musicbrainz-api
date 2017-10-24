from django.core.urlresolvers import resolve

from rest_framework.test import APITestCase

from collections.models import Collection, Record
from experiments.models import Musician

class CollectionAPITestCase(APITestCase):
    
    def setUp(self):
        self.lemonade = Collection.objects.create(name='Lemonade')
        self.humanz = Collection.objects.create(name='Humanz')
    
    def test_album_list_route(self):
        ''' Test that we have got routing setup for Collections '''
        route = resolve('/collections/')
        
        self.assertEqual(route.func.__name__, 'CollectionViewSet')
        
    def test_list_collections(self):
        ''' Test that we can get a list of collections '''
        response = self.client.get('/collections/')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], 'Humanz')
        self.assertEqual(response.data[1]['url'], 'http://testserver/collections/1/')
    
class RecordAPITestCase(APITestCase):
    
    def setUp(self):
        self.eyelid_movies = Collection.objects.create(name='Eyelid Movies', slug='eyelig-movies')
        self.futuristic_casket = Collection.objects.create(name='Futuristic Casket', slug='futuristic-casket',
                                                           album=self.eyelid_movies)
