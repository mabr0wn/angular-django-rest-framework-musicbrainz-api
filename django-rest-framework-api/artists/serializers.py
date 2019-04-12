# Django
from django.utils.text import slugify
# Django rest
from rest_framework import serializers
# Local
from artists.models import Artist


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        read_only_fields = ('slug',)

    def validate(self, data):
        data['slug'] = slugify(data['artist'])
        return data
