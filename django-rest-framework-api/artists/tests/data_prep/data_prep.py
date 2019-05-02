# Django
from django.contrib.auth.models import User
# Local
from artists.models import Artist, Album, Track

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
    {'id': 'artist_id_1', 'artist': 'test_artist_1'},
    {'id': 'artist_id_2', 'artist': 'test_artist_2'},
    {'id': 'artist_id_3', 'artist': 'test_artist_3'},
]

ALBUMS = [
    {'id': 'album_id_1', 'name': 'test_album_1', 'artist': 'test_artist_1',' image': 'http://imageurl1.com', },
    {'id': 'album_id_2', 'name': 'test_album_2'},
    {'id': 'album_id_3', 'name': 'test_album_3', 'image': ''},
]

LOGGED_IN_USER = USERS[1]

def create_():
    user1 = User.objects.create(**USERS[0])
    user2 = User.objects.create(**USERS[1])

    artist1 = Artist.objects.create(artist='test_artist_1')
    artist2 = Artist.objects.create(artist='test_artist_2')

    album1 = Album.objects.create(**ALBUMS[0])
    album1.lists.add(artist1)
    album2 = Album.objects.create(**ALBUMS[1])
    album2.lists.add(artist1, artist2)
    album3 = Album.objects.create(**ALBUMS[2])
    album3.lists.add(artist2)

    artist1 = Artist.objects.create(**ARTISTS[0])
    artist1.track.add(album1)
    artist2 = Artist.objects.create(**ARTISTS[1])
    artist2.track.add(album2, album3)
    artist3 = Artist.objects.create(**ARTISTS[2])
    artist3.track.add(album3)

def expected_artists():
    return ARTISTS


def expected_albums():
    artists = expected_artists()
    albums = [{**album} for album in ALBUMS]
    albums[0]['artistTrack'] = [artists[0]]
    albums[1]['artistTrack'] = [artists[1]]
    albums[1]['image'] = ''
    albums[2]['artistTrack'] = [artists[1], artists[2]]
    return albums

def expected_artist():
    albums = expected_albums()
    artists = [
        {
            'artist': ARTISTS[0]['artist'],
            'albums': [albums[0], albums[1]],
            'track': 'test track 1'
        },
        {
            'artist': ARTISTS[1]['artist'],
            'albums': [albums[1], albums[2]],
            'track': 'test track 2'
        },
        {
            'artist': ARTISTS[0]['artist'],
            'albums': [albums[2]],
            'track': 'unnamed track'
        }
    ]
    return lists

