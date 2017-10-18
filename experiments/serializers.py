from rest_framework import serializers
from experiments.models import Experiment, LANGUAGE_CHOICES, STYLE_CHOICES

"""
Replace the ExperimentSerializer class with the following.

Update our serializer,

Now that experiments are associated with the user that created them, let's update our ExperimentSerializer
to reflect that.
"""
class ExperimentSerializer(serializers.HyperlinkedModelSerializer):
  ''' we can also use CharField(read_only=True) && will set it to read only '''
  owner = serializers.ReadOnlyField(soruce='owner.username')
  ''' HyperLinkedIdentitField used to represent the target of the relationship using a hyperlink
      Will allow the serialized data to show a hyperlink for highlight and point it to view name
      experiment-highlight and format it in HTML        '''
  highlight = serializers.HyperLinkedIdentityField(view_name='experiment-highlight', format='html')
  
  class Meta:
    model = Experiment
    # Many=True will call below instead of the model.
    fields = ('url', 'id', 'highlight',  'owner',
              'title', 'code', 'linenos', 'language', 'style',)
    
    
    
from django.contrib.auth.models import User

"""
Now we need to add a User serializer to work with Users, we will add a representation of those users
to our API.  We create this to see how many JSON each user has created, it will display the id, username
and the number of experiments that user created.

Because 'experiments' is a reverse relationship on the User model, it will not be included by default
when using the ModelSerializer class, so we need to add an explicit field for it.
"""

class UserSerializer(serializer.HyperlinkedModelSerializer):
  experiments = serializers.PrimaryKeyRelatedField(many=True, queryset=Experiment.objects.all())
  
  class Meta:
      model = User
      fields = ('url', 'id', 'username', 'experiments')




# class SnippetSerializer(serializers.Serializer):
# 	id = serializers.IntegerField(read_only=True)
# 	title = serializers.CharField(required=False, allow_blank=True, max_length=100)
# 	code = serializers.CharField(style={'base_template': 'textarea.html'})
# 	linenos = serializers.BooleanField(required=False)
# 	language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
# 	style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

# 	def create(self, validate_data):
# 		"""
# 		Create and return a new 'Snippet' instance, given the validated data.
# 		"""
# 		return Snippet.objects.create(**validate_data)

# 	def update(self, instance, validate_data):
# 		"""
# 		Update and return an existing 'Snippet' instance, given the validate_data.
# 		Checks to see if the data we entered below is valid.
# 		"""
# 		instance.title = validate_data.get('title', instance.title)
# 		instance.code = validate_data.get('code', instance.code)
# 		instance.linenos = validate_data.get('linenos', instance.linenos)
# 		instance.language = validate_data.get('language', instance.language)
# 		instance.style = validate_data.get('style', instance.style)
# 		instance.save()
# 		return instance    
