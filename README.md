# Django-serialization-001

![alt text](https://ksr-ugc.imgix.net/assets/011/705/984/4ea78430d3ad7dc88106a7b973248ba7_original.jpg?w=460&fit=max&v=1463687041&auto=format&q=92&s=18c6f5574a0053aa1934f0845f4dd4bb)

![alt text](https://github.com/mattd429/Django-serialization-001/blob/master/experiments/img/Screen%20Shot%202017-10-19%20at%204.29.04%20PM.png)

![alt text](https://github.com/mattd429/Django-serialization-001/blob/master/experiments/img/Screen%20Shot%202017-10-19%20at%204.29.51%20PM.png)

![alt text](https://github.com/mattd429/Django-serialization-001/blob/master/experiments/img/Screen%20Shot%202017-10-19%20at%204.30.20%20PM.png)

create a Django project including serialization to serializing and deserializing the experiment instances into representations such as `json`

- Web API 

REST framework, and give you a comprehensive understanding of how everything fits together. we need to use serialization to store instances for representation of `JSON`

- We can do this by declaring serializers that work very similar to Django's forms
- Create a `models.py` to have that data be serialized in `serializers.py`

```python
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Experiment(models.Model):
	owner = models.ForeignKey('auth.User', related_name='experiments', on_delete=models.CASCADE)
	highlighted = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	code = models.TextField()
	linenos = models.BooleanField(default=False)
	language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
	style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

	def save(self, *args, **kwargs):
    lexer = get_lexer_by_name(self.language)
		linenos = self.linenos and 'table' or False
		options = self.title and {'title': self.title} or {}
		formatter = HtmlFormatter(style=self.style, linenos=linenos,
								  full=True, **options)
		self.highlighted = highlight(self.code, lexer, formatter)
		super().save(*args, **kwargs)

	
	class Meta:
		ordering = ('created',)
```
- Create a `serializers.py` to serialize the db fields in `models.py` into `JSON`

```python
class ExperimentSerializer(serializers.HyperlinkedModelSerializer):

	owner = serializers.ReadOnlyField(source='owner.username')
	highlight = serializers.HyperlinkedIdentityField(view_name='experiment-highlight', format='html')

	class Meta:
		model = Experiment
		fields = ('url', 'id', 'highlight', 'owner', 
				  'title', 'code', 'linenos', 'language', 'style', )

class UserSerializer(serializers.HyperlinkedModelSerializer):
	experiments = serializers.HyperlinkedRelatedField(many=True, view_name='experiment-detail', read_only=True)

	class Meta:
		model = User
		fields = ('url', 'id', 'username', 'snippets')
```
