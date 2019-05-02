# Django
from django.contrib.auth.models import User
# Local
from artists.model import Artist, Album, Track

# EXPECTED DATA

#   artist1 - album1 - track1
#                    /
#   artist2 - album2 - track2
#           \        /
#   artist3 - album3 - track3


USERS = [
    {'username': 'user1', 'password': 'password1'},
    {'username': 'user2', 'password': 'password2'}
]

ARTISTS = [
    {'id': 'artist_id_1', 'name': 'test_artist_1'},
    {'id': 'artist_id_2', 'name': 'test_artist_2'},
    {'id': 'artist_id_3', 'name': 'test_artist_3'},
]

ALBUMS = [
    {'id': 'album_id_1', 'title': 'test_album_1',
     'image': 'http://imageurl1.com'},
    {'id': 'album_id_2', 'title': 'test_album_2'},
    {'id': 'album_id_3', 'title': 'test_album_3', 'image': ''},
]
