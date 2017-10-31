from django.test import LiveServerTestCase
# Not guarentee that the user model is loaded into app cache.
from django.contrib.auth import get_user_model

from selenium import webdriver

from expeirments.models import Musician
from collections.models import Collection, Record

class StudentTestCase(LiveServerTestCase):
    ''' Tell the webdriver to poll the Document object model to chrome and wait 2 seconds '''
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicity_wait(2)
        
        self.colletion1 = Collection.objects.create(name='The Fame', slug='the-fame')
        self.record1 = Record.objects.create(name='Just Dance', slug='just-dance')
        self.musician1 = Musician.objects.create(genre='pop', artist='Lady Gag', track=self.track1,
                                                 slug='lady-gaga')
        self.collection2 = Collection.objects.create(name='Voices', slug='voices')
        self.record2 = Record.objects.create(name='Black Out Days', slug='black-out-days')
        self.musician2 = Musician.objects.create(genre='electronic', artist='Phantogram', track=self.track2,
                                                 slug='phantogram')
        self.collection3 = Collection.objects.create(name='Late Registration', slug='late-registration')
        self.record3 = Record.objects.create(name='I Need to Know', slug='i-need-to-know')
        self.musicians3 = Musician.objects.create(genre='hiphop', artist='Kanye West', track=self.track3,
                                                 slug='kayne-west')
