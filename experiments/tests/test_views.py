from unittest.mock import patch, Mock

from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet

from experiments.views import index, musician_detail
from experiments.models import Musician
from collections.models import Collection, Record

class MusicianBaseTestCase(TestCase):
    
    def setUp(self):
        # Returns a request
        self.factory = RequestFactory()
        
        @classmethod
        def setUpClass(cls):
            super().setUpClass()
            cls.voices = Collection.objects.create(name='Voices', slug='voices')
            cls.nothing_but_trouble = Record.objects.create(name='Nothing but Trouble', slug='nothing-but-trouble', album=cls.voices)
            cls.electropop_musician = Musician.objects.create(genre='electropop', artist='Phantogram', track=cls.nothing_but_trouble,
                                                              slug='phantogram')
            
