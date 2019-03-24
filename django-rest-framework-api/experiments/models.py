from django.db import models
from Collection.models import Collection, Record
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.core.urlresolvers import reverse
import musicbrainzngs as mb
from django.utils.text import slugify

"""
A Lexer splits the source into tokens, fragments of the source that have a 
token type that determines what the text represents semantically
(e.g., keyword, string, or comment). There is a lexer for every language or markup
format that Pygments supports
"""

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

mb.set_useragent('Mbrown - mattd429@gmail.com', version='0.0.1')

class Musician(models.Model):
    record = models.ForeignKey(Record)
    artist = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    start_time = models.CharField(max_length=20, blank=True, null=True)
    end_time = models.CharField(max_length=20, blank=True, null=True)
    slug = models.SlugField()
    
    class Meta:
        ordering = ['record', 'start_time']
    
    def get_absolute_url(self):
        return reverse('musician_detail_view', kwargs={'collection': self.record.collection.slug, 'record': self.record.slug,
                                                       'artist': self.slug})
    def get_period_of_play_time(self):
        play_string = ''
        if self.start_time and self.end_time:
            play_string = '{}-{}'.format(self.start_time, self.end_time)
        return play_string
    ''' From MusicBrainzNGS '''
    @classmethod
    def get_artist_records_from_musicbrainz_api(cls, artist):
        """
        Create Collection, Record, and Musician reords for artists we find
        in the MusicBrainzNGS API
        
        :param artist: an artist's name as a string to search for
        :return: Queryset of Musicians
        """
        search = mb.search_artists(artist)
        results = search['artist-list'][0]
        genre = Musician.get_genre_from_musicbrainz_tag_list(results['tag-list'])
        
        for collection_dict in mb.browse_releases(results['id'], includes=['recordings'])['release-list']:
            collection = Collection.objects.create(name=collection_dict['title'], artist=artist, slug=slugify(collection['title'])))
            
            """
                Medium-list results from dearch having an additional 
                <track-count> elements containing the number of
                tracks over all mediums.
                e.g. CD 1 of the 1984 US release of "The Wall" by Pink Floyd

            """
            
            for record_dict in collection_dict['medium-list'][0]['track-list']:
                record = Record.objects.create(collection=collection, name=record_dict['recording']['title'],
                                               record_number=record_dict['position'],
                                               slug=slugify(record_dict['recording']['title']))
                Musician.objects.create(record=record, artist=artist, genre=genre, slug=slugify(artist))
                
            return Musician.objects.filter(artist=artist)
    @classmethod
    def get_genre_from_musicbrainz_tag_list(cls, tag_list):
        """
        Return a genre from a list of dict-tags as returned in the
        MusicBrainzNGS API
        
        :param tag_list: a list of dicts with keys 'count' and 'name'
        :return: a string
        """
        map = {'electropop': 'electropop', 'pop': 'pop', 'electronic': 'electronic'}
        return map[set(map.keys()).intersection([tag['name'] for tag in tag_list]).pop()]
    

class Experiment(models.Model):
    owner = models.ForeignKey('auth.User', related_name='experiments', on_delete=model.CASADE)
    highlighted = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_lenth=100)
      
    """
    Use the 'pygments' library to create a highlighted HTML
    representation of the code experiment.
    
    above *args and **kwargs is calling the Experiment fields and
    the values assigned to those fields.
    
    This method def save() below allows to create highlighted HTML format,
    calling itself, with the *args && **kwargs listed in the experiment
    class above from there we call the lexer which will define the language(python)
    you selected for your highlighter, linenos which allows you to add number lines by
    default this option will be false.  Options will display the title you input in
    the highlighted html.  formatter will place the format into HTML style.
    
    self.highlight will highlight anything in model field listed, in our case it is
    code, lexer, formatter.
    super().save will call to our model class Experiment save it with any info
    we want to update it with by using the *args && **kwargs to be able to save to the
    fields in model Experiment with any updates we may change.
    
    Highlighting is a way to display code in different colors && fonts.  it will
    allow the programmer to see errors much more clearly.
    """
    def save(self, *args, **kwargs):  

        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenoe=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ('created',)
