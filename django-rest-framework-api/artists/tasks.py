# Django
from django.utils.text import slugify
# Celery
from celery import shared_task
# Local
from .models import Artist, Album, Record
# Musicbrainz
import musicbrainzngs as mb

mb.set_useragent('Mbrown - mattd429@gmail.com', version='1.0.1')


@shared_task
def get_artist_tracks_from_musicbrianz_api(artist):
    search_results = mb.search_artists(artist)
    best_result = search_results['artist-list'][0]
      
    genre = Artist.get_genre_from_musicbrainz_tag_list(best_result['tag-list'])
    
    for album_dict in mb.browse_releases(best_result['id'], includes=['recordings'])['release-list']:
        album = Album.objects.create(name=album_dict['title'], artist=artist, slug=slugify(album_dict['title']))
        
        for record_dict in album_dict['medium-list'][0]['track-list']:
            record = Record.objects.create(album=album, name=record_dict['recording']['title'],
                                           record_number=record_dict['position'],
                                           slug=slugify(record_dict['recording']['title']))
            
            Artist.objects.create(record=record, artist=artist, genre=genre, slug=slugify(artist))
            
    return Artist.objects.filter(artist=artist)
