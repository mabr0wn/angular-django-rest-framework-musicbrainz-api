# Pytest
import pytest
# Django
from django.core.management import call_command
# Local
from artists.models import Artist, Album, Track
# Mixer
from mixer.backend.django import Mixer

# We need to do this so that writing to the DB is possible in our tests.
pytestmark = pytest.mark.django_db

@pytest.fixture(autouse=True)
def mixer(request):
    call_command('migrate', interactive=False, verbosity=0)
    request.addfinalizer(lambda: call_command('flush', interactive=False, verbosity=0))
    return Mixer()

def test_base():
    from mixer.backend.django import mixer
    
    # Generate model with some values
    album = mixer.blend(Album, 
        name='Random Access Memories',
        artist='Daft Punk',
        image='https://www.wearevinyl.co.uk/collections/artists/products/daft-punk-random-access-memories',
        slug='random-access-memories'
    )
    track = mixer.blend(Track, 
        name='Give Life Back to Music',
        album=album,
        track_number=1,
        slug='give-life-back-to-music'
    )
    artist = mixer.blend(Artist, 
        track=track,
        artist='Daft Punk',
        genre='electronic',
        start_time='0:16',
        end_time='4:34',
        slug='daft-punk'
    )
    # print the results
    print(album.name, album.artist, album.image, album.slug)
    print(track.name, track.album, track.track_number, track.slug)
    print(artist.track, artist.artist, artist.genre, artist.start_time, artist.end_time, artist.slug)

    # assert that album name is equaled to string
    assert album.name == 'Random Access Memories'

    # Test the basic functionality of artist
    assert artist.artist == 'Daft Punk'
    assert artist.end_time == '4:34'

    # Test the duration of an Artist
    assert artist.get_period_of_play_time() == '0:16-4:34'


def test_album_fields(mixer):
    pass

def test_track_fields(mixer):
    pass

def test_artist_fields(mixer):
    pass
    
def test_get_genre_from_musicbrainz_tag_list(mixer):
    # will save to test DB.
    artist = mixer.blend('artists.Artist')
    ''' Test that we can map tags from musicbrainz to genres '''
    tag_list = [{'count': '3', 'name': 'electro'}]
    
    assert artist.get_genre_from_musicbrainz_tag_list(tag_list), 'electropop'
