from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.crsf import crsf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from experiments.models import Experiment
from experiments.serializers import ExperimentSerializer

# exempt from crsf for out peeps who dont have crsf
@crsf_exempt
def experiment_list(request):
  """
  list all code experiments, or create a new experiment.
  """
  # if the request is getting data.
  if request.method == 'GET':
    # List all experiments
    experiments = Experiment.objects.all()
    # call to the serializer class ExperimentSerializer
    # serializer queryset instead of model instance by using many=True
    serializer = ExperimentSerializer(experiments, many=True)
    # Return the data in JSON response, helper that wraps response data with
    # metadata about the response status.
    return JsonResponse(serializer.data, safe=False)
  
  elif request.method == 'POST':
    # Break down the JSON data from the request and post it.
    data = JSONParser().parse(request)
    # Create the new data in serializer
    serializer = ExperimentSerializer(data=data)
  
