# # Django
# from django.urls import resolve
# # Django rest
# from rest_framework.test import APITestCase
# # Local
# from Album.models import Album, Record
# from artists.models import Artist

# class AlbumAPITestCase(APITestCase):
    
#     def setUp(self):
#         self.lemonade = Album.objects.create(name='Lemonade')
#         self.humanz = Album.objects.create(name='Humanz')
    
#     def test_album_list_route(self):
#         ''' Test that we have got routing setup for set '''
#         route = resolve('/set/')
        
#         self.assertEqual(route.AlbumViewSet, 'set')
        
#     def test_list_set(self):
#         ''' Test that we can get a list of set '''
#         response = self.client.get('/set/')
        
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.AlbumViewSet, 'Humanz')
#         # self.assertEqual(response.data[0]['name'], 'Humanz')
#         # self.assertEqual(response.data[1]['url'], 'http://testserver/set/1/')
    
# class RecordAPITestCase(APITestCase):
    
#     def setUp(self):
#         self.eyelid_movies = Album.objects.create(name='Eyelid Movies', slug='eyelig-movies')
#         self.futuristic_casket = Album.objects.create(name='Futuristic Casket', slug='futuristic-casket',
#                                                            record=self.eyelid_movies)
#         self.electropop_artist = Artist.objects.create(genre='electropop', creator='Phantogram',
#                                                            slug='phantogram', record=self.futuristic_casket)
#     def test_retrieve_record(self):
#         ''' Test that we can get a list of records '''
#         response = self.client.get('/records/')
        
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data[0]['name'], 'Futuristic Casket')
#         self.assertEqual(response.data[0]['url'], 'http://testserver/records/1/')
   
#     def test_album_list_route(self):
#         ''' Test that we've got routing setup for set '''
#         route = resolve('/records/1/')
        
#         self.assertEqual(route.func.__name__, 'RecordViewSet')
