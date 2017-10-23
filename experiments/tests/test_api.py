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
    
    def test_musician_list_route(self):
        ''' Test that we've got routing set up for Musicians '''
        route = resolve('/api/musicians/')
        
        self.assertEqual(route.func.__name__, 'MusicianViewSet')
        
class ExperimentAPITestCase(APITestCase):
    
    def setUp(self):
        self.title_code = Experiment.objects.create(title='Experiment Title', code='var = 2'),
        self.language_style = Experiment.objects.create(language='Cucumber', style='autumn'),
    
    def test_create_experiment(self):
        ''' Test that we can create an Experiment '''
        post_data = {'url': 'http://127.0.0.1:8000/experiments/1/', 'id': 1,
                     'highlighted': 'http://127.0.0.1:8000/experiments/1/highlight/', 'owner': 'owner',
                     'title': 'Django Rest framework 3', 'code': '@api_view(['GET'])\r\ndef api_root(request, format=None):\r\n      return Response({\r\n      \t\t'users': reverse('user-list', request=request, format=format),\r\n\t\t'experiments': reverse('experiment-list', request=request, format=format)\r\n      })', 
                     'linenoe': False, 'language': 'python3', 'style': 'colorful'}
        response = self.client.post('/api/experiments/', data=post_data, format='html')
        
        self.assertEqual(response.status_code, 201, response.data)
        self.assertEqual(response_data, {
            'url': 'http://127.0.0.1:8000/experiments/1/',
            'id': 1,
            'highlight': 'http://127.0.0.1:8000/experiments/1/highlight/',
            'owner': 'owner',
            'title': 'Django is cool',
            'code': '@api_view(['GET'])\r\ndef api_root(request, format=None):\r\n      return Response({\r\n      \t\t'users': reverse('user-list', request=request, format=format),\r\n\t\t'experiments': reverse('experiment-list', request=request, format=format)\r\n      })',
            'linenos': False,
            'language': 'python3',
            'style': 'colorful'
        })
        
