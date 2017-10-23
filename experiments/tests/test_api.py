from django.core.urlresolvers import resolve

from rest_framework.test import APITestCase

from experiments.models import Experiment, LANGUAGE_CHOICES, STYLE_CHOICES,
from collections.models import Collection, Record,

class MusicianAPITestCase(APITestCase):
    
    def setUp(self):
        self.movement = Collections.objects.create(name='Movement', slug='movement')
        self.dreams_never_end = Record.objects.create(name'Dreams Never End', slug'dreams-never-end', collection=self.movement)
        
    def test_create_musician(self):
        """
        Test that we can create a musician
        """
        post_data = {'record': '/api/records/1/', 'creator': 'New Order', 'genre': 'electronic',
                     'start_time': '0:16', 'end_time': '3:15'}
        ''' Post the data into musicians in the format of json '''
        response = self.client.post('/api/musicians/', data=post_data, format='json')
        
        self.assertEqual(response.status_code, 201, response.data)
        self.assertEqual(response_data, {
            'url': 'http://127.0.0.1:8000/api/musicians/1/',
            'creator': 'New Order',
            'slug': 'new-order',
            'genre': 'electronic',
            'start_time': '0:16',
            'end_time': '3:15',
            'record':  'http://127.0.0.1:8000/api/tracks/1/'
        })
        
