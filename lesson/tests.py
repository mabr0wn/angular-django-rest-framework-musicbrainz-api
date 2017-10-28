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
        
        self.colletion1 = Collection.objects.create(name='', slug='')
        self.record1 = Record.objects.create(name='', slug='')
        self.musician1 = Musician.objects.create(genre='', artist='', track=self.track1,
                                                 slug='')
