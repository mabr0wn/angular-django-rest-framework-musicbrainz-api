# Django
from django.test import TestCase
# VCR
from vcr import VCR
# Tasks
from artists.tasks import get_artist_tracks_from_musicbrianz_api

albums_vcr = VCR(cassette_library_dir='artists/tests/vcr_cassettes')

class SoloTaskTestCase(TestCase):

    def test_get_artist_tracks_from_musicbrainz(self):
        """
        Test that we can make Solos from the MusicBrainz API
        """
        with albums_vcr.use_cassette('search-madonna.yml'):
            created_solos = get_artist_tracks_from_musicbrianz_api('Madonna')

        self.assertEqual(len(created_solos), 135)
        self.assertEqual(created_solos[0].artist, 'Madonna')
        self.assertEqual(created_solos[1].record.name, 'Angel')

    def test_slugify_max_length(self):
        """
        Test that we can handle slugifying track titles that are longer than 50 chars
        """
        with albums_vcr.use_cassette('search-oscar-peterson.yml'):
            queryset = get_artist_tracks_from_musicbrianz_api('Oscar Peterson')

        self.assertEqual(queryset.count(), 240)


    def test_genre_tag_map(self):
        """
        Test that we set genre to 'unknown' if we do not have a reliable mapping for MB tags
        """
        with albums_vcr.use_cassette('search-miles-davis.yml'):
            queryset = get_artist_tracks_from_musicbrianz_api('Miles Davis')

        self.assertEqual(queryset[0].genre, 'unknown')