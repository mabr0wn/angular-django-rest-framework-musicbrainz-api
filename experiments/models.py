from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.utils import timezone

# Pygments is used for code highlighting

"""
A Lexer splits the source into tokens, fragments of the source that have a 
token type that determines what the text represents semantically
(e.g., keyword, string, or comment). There is a lexer for every language or markup
format that Pygments supports
"""

# get_all_lexers() returns an iterable over all registeed lexers, yeilding tuples in the format.
# call item in get_all_lexers() if item list[1] is one.
LEXERS = [item for item in get_all_lexers() if item[1]]
# sort the items in LEXERS and this will list the **kwargs in a pair[('Clipper', 'FoxPro')]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# sorting the items in get_all_styles()
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Experiment(models.Model):
    created = models.DateTimeField(editable=False)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_lenth=100)
      
    # *args would be to call as many arguments as you want to throw at it.
    # e.g. "one", "two", "three"
    # **kwargs would be calling items in a dictionary format we would need to call
    # it like a dictionary for item in kwargs.items() will print the items out in pairs
    # with *args and **kwargs we can pass in a unlimited amount of arguments, and keyword arguments
    # Note that *args much come beofre **kwargs or program will not compile. 
    def save(self, *args, **kwargs):
      ''' On Save, update timestamps '''
      if not self.id:
          self.created = timezone.now()
      return super().save(*args, **kwargs)
    # order by data created
    class Meta:
      ordering = ('created',)
