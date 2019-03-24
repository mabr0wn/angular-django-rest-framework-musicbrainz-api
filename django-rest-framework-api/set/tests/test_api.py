from django.core.urlresolvers import resolve

from rest_framework.test import APITestCase

from set.models import Collection, Record
from experiments.models import Musician

class CollectionAPITestCase(APITestCase):
    
    def setUp(self):
        self.lemonade = Collection.objects.create(name='Lemonade')
        self.humanz = Collection.objects.create(name='Humanz')
    
    def test_album_list_route(self):
        ''' Test that we have got routing setup for set '''
        route = resolve('/set/')
        
        self.assertEqual(route.func.__name__, 'CollectionViewSet')
        
    def test_list_set(self):
        ''' Test that we can get a list of set '''
        response = self.client.get('/set/')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], 'Humanz')
        self.assertEqual(response.data[1]['url'], 'http://testserver/set/1/')
    
class RecordAPITestCase(APITestCase):
    
    def setUp(self):
        self.eyelid_movies = Collection.objects.create(name='Eyelid Movies', slug='eyelig-movies')
        self.futuristic_casket = Collection.objects.create(name='Futuristic Casket', slug='futuristic-casket',
                                                           collection=self.eyelid_movies)
        self.electropop_musician = Musician.objects.create(genre='electropop', creator='Phantogram',
                                                           slug='phantogram', record=self.futuristic_casket)
    def test_retrieve_record(self):
        ''' Test that we can get a list of records '''
        response = self.client.get('/records/')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], 'Futuristic Casket')
        self.assertEqual(response.data[0]['url'], 'http://testserver/records/1/')
   
    def test_collection_list_route(self):
        ''' Test that we've got routing setup for set '''
        route = resolve('/records/1/')
        
        self.assertEqual(route.func.__name__, 'RecordViewSet')
