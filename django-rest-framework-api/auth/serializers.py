# Django
from django.contrib.auth.models import User
# Django rest
from rest_framework import serializers



"""
Now we need to add a User serializer to work with Users, we will add a representation of those users
to our API.  We create this to see how many JSON each user has created, it will display the id, username
and the number of Artist that user created.

Because 'artists' is a reverse relationship on the User model, it will not be included by default
when using the ModelSerializer class, so we need to add an explicit field for it.
"""

class UserSerializer(serializers.HyperlinkedModelSerializer):
#   artists = serializers.PrimaryKeyRelatedField(many=True, queryset=Experiment.objects.all())
  
  class Meta:
      model = User
      fields = ('url', 'id', 'username')