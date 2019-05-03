# Pytest
import pytest
# Mock
from unittest import TestCase
# Local
from ..serializers import ArtistSerializer

# We need to do this so that writing to the DB is possible in our tests.
pytestmark = pytest.mark.django_db

class ArtistSerializerTest(TestCase):

    def test_validate(self):
        serializer = ArtistSerializer()
        data = serializer.validate({'artist': 'Ray Brown'})

        self.assertEqual(data, {
            'artist': 'Ray Brown',
        })
