# Pytest
import pytest
from mixer.backend.django import Mixer
# Django
from django.core.management import call_command
# Local
from ..serializers import ArtistSerializer

# We need to do this so that writing to the DB is possible in our tests.
pytestmark = pytest.mark.django_db

@pytest.fixture(autouse=True)
def mixer(request):
    call_command('migrate', interactive=False, verbosity=0)
    request.addfinalizer(lambda: call_command('flush', interactive=False, verbosity=0))
    return Mixer()

def test_validate(mixer):
    serializer = ArtistSerializer()
    data = serializer.validate({'artist': 'LoFi Hip Hop'})

    assert data == {'artist': 'LoFi Hip Hop' }
