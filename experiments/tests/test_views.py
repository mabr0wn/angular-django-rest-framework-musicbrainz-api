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
            cls.nothing_but_trouble = Record.objects.create(name='Nothing but Trouble', slug='nothing-but-trouble', collection=cls.voices)
            cls.electropop_musician = Musician.objects.create(genre='electropop', creator='Phantogram', track=cls.nothing_but_trouble,
                                                              slug='phantogram')
            cls.permanent_signal = Collection.objects.create(name='Permanent Signal', slug='permanent-signal')
            cls.the_way_out = Record.objects.create(name='The Way Out', slug='the-way-out', collection=cls.permanent_signal)
            cls.dream_pop_musician = Musician.objects.create(genre='dream pop', creator='Procelain Raft', record=cls.the_way_out,
                                                             slug='procelain-raft')
            
