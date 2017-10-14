from rest_framework import serializers
from experiments.models import Experiment, LANGUAGE_CHOICES, STYLE_CHOICES

"""
Replace the ExperimentSerializer class with the following.
"""
class ExperimentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Experiment
    # Many=True will call below instead of the model.
    fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

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
