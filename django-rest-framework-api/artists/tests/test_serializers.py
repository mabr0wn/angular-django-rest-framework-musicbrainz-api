# Pytest
import pytest
# Mock
from unittest import TestCase
# Local
from ..models import Track, Album, Artist
from ..serializers import TrackSerializer, AlbumSerializer, ArtistSerializer
from .data_prep import data_prep

# We need to do this so that writing to the DB is possible in our tests.
pytestmark = pytest.mark.django_db

class ArtistSerializerTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        data_prep.create_()
        cls.expected_artists = data_prep.expected_artists()

    def test_all_fields_in_serialized_artist(self):
        artist = Artist.objects.create(artist='test_artist_1')
        Artist.objects.get(artist='test_artist_1')
        serialized = ArtistSerializer(artist)
        self.assertEqual(serialized.data, self.expected_artists[0])
