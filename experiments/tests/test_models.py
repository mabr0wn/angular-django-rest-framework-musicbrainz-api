from unittest.mock import patch

from django.test import TestCase

from experiments.models import Musician, Experiment
from collections.model import Collection, Record

""" SetUp the TestCase """

class MusicianModelTestCase(TestCase):
    
    def setUp(self):
        self.collection = Collection.objects.create(
            name='Random Access Memories',
            creator='Daft Punk',
            slug='random-access-memories'
         )
         self.record = Musician.objects.create(
             name='Give Life Back to Music',
             collection=self.collection,
             track_number=1,
             slug='give-life-back-to-music'
         )
         
         self.musician = Musician.objects.create(
             record=self.reord,
             creator='Daft Punk',
             genre='electronic',
             start_time='0:16',
             end_time='4:34',
             slug='daft-punk'
         )     
