# # Mock
# from unittest import TestCase
# # Local
# from artists.serializers import ArtistSerializer

# class ArtistSerialierTestCase(TestCase):
  
#     def test_validate(self):
#         ''' Test that ArtistSerializer.validate() adds a slugged version of the artist attribute to the data '''
#         serializer = ArtistSerializer()
#         data = serializer.validate({'creator:' 'Trey Songs'})
        
#         self.assertEqual(data, {
#             'creator': 'Trey Songz',
#             'slug': 'trey-songz'
#         })
