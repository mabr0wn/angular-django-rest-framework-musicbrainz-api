# Django
from django.urls import resolve
from django.utils.encoding import force_text
# Pytest
import pytest
# Django rest
from rest_framework.test import APITestCase
# Local
from artists.models import Artist, Album, Track

class ArtistAPITestCase(APITestCase):
    
    def setUp(self):
        self.movement = Album.objects.create(name='Movement', slug='movement')
        self.dreams_never_end = Track.objects.create(name='Dreams Never End', slug='dreams-never-end', album=self.movement)

    def test_create_artist(self):
        """
        Test that we can create a artist
        """
        post_data = {'track': '/api/tracks/1/', 'artist': 'New Order', 'slug': 'new-order', 'genre': 'electronic',
                     'start_time': '0:16', 'end_time': '3:15'}
        ''' Post the data into artists in the format of json '''
        response = self.client.post('/api/artists/', data=post_data, format='json')
        
        self.assertEqual(response.status_code, 201, response.data)
        self.assertEqual(response.data, {
            'url': 'http://testserver/api/artists/1/',
            'artist': 'New Order',
            'slug': 'new-order',
            'genre': 'electronic',
            'start_time': '0:16',
            'end_time': '3:15',
            'track':  'http://testserver/api/tracks/1/'
        })
    
    def test_artist_list_route(self):
        ''' Test that we've got routing set up for artists '''
        route = resolve('/api/artists/')
        
        self.assertEqual(route.func.__name__, 'ArtistViewSet')

class AlbumAPITestCase(APITestCase):
    
    def setUp(self):
        self.lemonade = Album.objects.create(name='Lemonade')
        self.humanz = Album.objects.create(name='Humanz')
    
    def test_album_list_route(self):
        ''' Test that we have got routing setup for set '''
        route = resolve('/api/albums/')
        
        self.assertEqual(route.func.__name__, 'AlbumViewSet')

    def test_list_albums(self):
        ''' Test that we can get a list of set '''
        response = self.client.get('/api/albums/')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], 'Humanz')
        self.assertEqual(response.data[1]['url'], 'http://testserver/api/albums/1/')
    
class TrackAPITestCase(object):
    def setUp(self):
        eyelid_movies = Album.objects.create(name='Eyelid Movies', slug='eyelig-movies')
        futuristic_casket = Track.objects.create(name='Futuristic Casket', slug='futuristic-casket',                                              album=self.eyelid_movies)
        electropop_artist = Artist.objects.create(genre='electropop', artist='Phantogram',
                                                           slug='phantogram', track=futuristic_casket)
    @pytest.mark.django_db                                                     
    def test_retrieve_track(self, client):
        ''' Test that we can get a list of tracks '''
        r = client.get('/api/tracks/')
        
        assert r.status_code == 200
        assert r.data[0]['name'] == 'Futuristic Casket'
        assert r.data[0]['url'] == 'http://testserver/api/tracks/1/'
       

    @pytest.mark.django_db 
    def test_album_list_route(self, client):
        ''' Test that we've got routing setup for set '''
        route = client.get('/api/tracks/1/')

        assert force_text(route.content) == 'TrackViewSet'