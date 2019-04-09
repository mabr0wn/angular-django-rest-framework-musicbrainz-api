# Django rest
from rest_framework import serializers
# Local
from experiments.models import Experiment, LANGUAGE_CHOICES, STYLE_CHOICES

"""
Replace the ExperimentSerializer class with the following.

Update our serializer,

Now that experiments are associated with the user that created them, let's update our ExperimentSerializer
to reflect that.
"""
class ExperimentSerializer(serializers.HyperlinkedModelSerializer):
  ''' we can also use CharField(read_only=True) && will set it to read only '''
  owner = serializers.ReadOnlyField(source='owner.username')
  ''' HyperLinkedIdentitField used to represent the target of the relationship using a hyperlink
      Will allow the serialized data to show a hyperlink for highlight and point it to view name
      experiment-highlight and format it in HTML        '''
  highlight = serializers.HyperlinkedIdentityField(view_name='experiment-highlight', format='html')
  
  class Meta:
    model = Experiment
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

class UserSerializer(serializers.HyperlinkedModelSerializer):
  experiments = serializers.PrimaryKeyRelatedField(many=True, queryset=Experiment.objects.all())
  
  class Meta:
      model = User
      fields = ('url', 'id', 'username', 'experiments')
