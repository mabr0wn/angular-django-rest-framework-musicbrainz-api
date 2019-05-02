from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from ..data_prep import data_prep

class APIViewTest(APITestCase):
    """"Test for GET all lists API"""

    def setUp(self):
        data_prep.create_()
        self.expected_lists = data_prep.expected_artist()
        self.expected_albums = data_prep.expected_albums()
        self.expected_artists = data_prep.expected_artists()

    def prepare_auth(self):
        test_user = User.objects.get(username='user2')
        self.client.force_authenticate(user=test_user)

    def clear_auto_generated_data(self, response_data):
        for field in ['created', 'lastUpdate', 'id']:
            del response_data[field]

    def clear_auto_generated_data_from_collection(self, response_collection):
        for item in response_collection:
            self.clear_auto_generated_data(item)