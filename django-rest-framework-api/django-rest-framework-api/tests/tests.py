# # Django
# from django.test import LiveServerTestCase
# # Not guarentee that the user model is loaded into app cache.
# from django.contrib.auth import get_user_model
# import time
# # Selenium
# from selenium import webdriver
# # Local
# from artists.models import Artist
# from albums.models import Album, Record

# class UserTestCase(LiveServerTestCase):
#     ''' Tell the webdriver to poll the Document object model to chrome and wait 2 seconds '''
#     def setUp(self):
#         self.browser = webdriver.Chrome('/Users/matthewbrown/downloads/chromedriver')
#         self.browser.get('http://www.google.com/xhtml')
#         time.sleep(5) # Let the user actually see something!
        
#         self.album1 = Album.objects.create(name='The Fame', slug='the-fame')
#         self.record1 = Record.objects.create(name='Just Dance', slug='the-fame')
#         self.artist1 = Artist.objects.create(genre='pop', artist='Lady Gag', record=self.record1,
#                                                  slug='lady-gaga')
#         self.album2 = Album.objects.create(name='Voices', slug='voices')
#         self.record2 = Record.objects.create(name='Black Out Days')
#         self.artist2 = Artist.objects.create(genre='electronic', artist='Phantogram', record=self.record2,
#                                                  slug='phantogram')
#         self.album3 = Album.objects.create(name='Late Registration', slug='late-registration')
#         self.record3 = Record.objects.create(name='I Need to Know')
#         # self.record3 = Record.objects.create(name='I Need to Know', slug='i-need-to-know')
#         self.artists3 = Artist.objects.create(genre='hiphop', artist='Kanye West', record=self.record3,
#                                                  slug='kayne-west')
        
#         self.artist4 = Artist.objects.create(genre='electropop', artist='Gorillaz', record=self.track2,
#                                                  slug='gorillaz', start_time='0:25', end_time='3:47')
#         record4 = Record.objects.create(name='My Only Friend', album=self.album2, record_number=11)
#         record5 = Record.objects.create(name='Never Going Home', album=self.album2, record_number=4)
        
#         self.admin_user = get_user_model().objects.create_superuser(username='username', email='example@example.com',
#                                                                     password='password')
        
#     def tearDown(self):
#         self.browser.quit()
        
#     def find_search_results(self):
#         return self.browser.find_elements_by_css_selector('.mb-search-result a')
    
#     def test_user_find_artists(self):
#         """
#         Test that a user can search for artists
#         """
#         # Sarah is a promoter who would like to find more hip hop composers so she can book new talent.
#         # Visits the homepage of website
#         home_page = self.browser.get(self.live_server_url + '/')
        
#         # She knows she's in the right place because she can see the name of the site in the heading.
#         brand_element = self.browser.find_element_by_css_selector('.navbar-brand')
#         self.assertEqual('MB', brand_element.text)
        
#         # She sees the inputs of the search form, including labels and placeholders.
#         genre_input = self.browser.find_element_by_css_selector('input#mb-genre')
#         self.assertIsNotNone(self.browser.find_element_by_css_selector('label[for="mb-genre"]'))
#         self.assertEqual(genre_input.get_attribute('placeholder'), 'Search Genre')
        
#         artist_input = self.browser.find_element_by_css_selector('input#mb-artist')
#         self.assertIsNotNone(self.browser.find_element_by_css_selector('label[for="mb-artist"]'))
#         self.assertEqual(artist_input.get_attribute('placeholder'), 'i.e. Maroon 5')
        
#         # She types too many search results...
#         search_results = self.find_search_results()
#         self.assertGreater(len(search_results), 2)
        
#         # So she adds an artist to her search query and gets more manageable list.
#         second_artist_input = self.browser.find_element_by_css_selector('input#mb-artist')
#         second_artist_input.send_keys('Phantogram')
#         self.browser.find_element_by_css_selector('form input').bind('<Return>')
        
#         second_search_results = self.find_search_results()
#         self.assertEqual(len(second_search_results), 2)
        
#         # She clicks on a search results.
#         second_search_results[0].click()
        
#         # On the composer page
#         self.assertEqual(self.browser.curren_url,
#              self.live_server_url + '/recordings/black-out-days/voices/phantogram/')
        
#         # She see the artist
#         self.assertEqual(self.browser.find_element_by_css_selector('#mb-artist').text, 'Phantogram')
        
        
    
        
        
