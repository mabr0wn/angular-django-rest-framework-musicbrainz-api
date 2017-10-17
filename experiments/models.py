from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

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
    
    This method def save below allows to create highlighted HTML format,
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
        formatter - HtmlFormatter(style=self.style, linenoe=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)
    
    # order by date created
    class Meta:
        ordering = ('created',)
