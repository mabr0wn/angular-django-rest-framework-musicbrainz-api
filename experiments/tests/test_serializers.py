from unittest import TestCase

from experiments.serializers import MusicianSerializer

class MusicianSerialierTestCase(TestCase):
  
    def test_validate(self):
        ''' Test that MusicianSerializer.validate() adds a slugged version of the artist attribute to the data '''
        serializer = MusicSerializer()
        data = serializer.validate({'creator:' 'Trey Songs'})
        
        self.assertEqual(data, {
            'creator': 'Trey Songz',
            'slug': 'trey-songz'
        })
