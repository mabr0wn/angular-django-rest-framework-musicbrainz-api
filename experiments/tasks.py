from django.utils.text import slugify

from celery import shared_task
import musicbrainzngs as mb

from .models import Musician
from collections.models import Collection, Record

mb.set_useragent('Set Content', version='0.0.1')

"""
The tasks you write will probably live in a reusable apps,
reusable apps cannot depend on the project itself, so you
also cannot import your app instance directly.

The @shared_task decarator lets you create tasks without
having any concrete app instance.
"""
@share_task
def get_artist_tracks_from_musicbrianz_api(artist):
    """
    Create Collection, Record, and Musician records for artists we find in the MusicBrainzNGS API
    
    :param artist: an artist's name as a string to search for
    :return: Queryset of Musicians
    """
    search_results = mb.search_artists(artist)
    best_result = search_results['artist-list'][0]
    
    if 'pop' not in [d['name'] for d in best_result['tag-list']]:
        return Musician.objects.none()
      
    genre = Musician.get_instrument_from_musicbrainz_tag_list(best_result['tag-list'])
    
    for collection_dict in mb.browse_releases(best_result['id'], includes=['recordings'])['release-list']:
        collection = Collection.objects.create(name=collection_dict['title'], artist=artist, slug=slugify(collection_dict['title']))
        
        for record_dict in collection_dict['medium-list'][0]['track-list']:
            record = Record.objects.create(collection=collection, name=record_dict['recording']['title'],
                                           record_number=record_dict['position'],
                                           slug=slugify(record_dict['recording']['title']))
            
            Musician.objects.create(record=record, artist=artist, genre=genre, slug=slugify(artist))
            
    return Musician.objects.filter(artist=artist)
