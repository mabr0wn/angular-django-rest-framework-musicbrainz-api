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
    # if it is valid save it
    if serializer.is_valid():
      serializer.save()
      # return the new data or give an error if not valid
      # 201 = created 
      return JsonReponse(serializer.data, status=201)
    # 400 = bad request
    return JsonResponse(serializer.errors, status=400)
  
  @crsf_exempt
  # request && primary_key
  def experiment_detail(request, pk):
    """
    Retreieve, update or delete a code experiment
    """
    try:
      experiment = Experiment.objects.get(pk=pk)
    except Experiment.DoesNotExist:
      # returns a http request page not found(404)
      return HttpResponse(status=404)
    
    # retrieve data
    if request.method == 'GET':
      serializer = ExperimentSerialzer(experiment)
      return JsonResponse(serializer.data)
    # Update data
    elif request.method == 'PUT':
      # data equals JSONParser, break down the data, parse the data request.
      data = JSONParser().parse(request)
      # update the serializer
      serializer = ExperimentSerializer(experiment, data=data)
      if serializer.is_valid():
          serializer.save()
          return JSONParser(serialzer.data)
       # 400 = bad request 
       return JSONParser(serializer.errors status=400)
      
    # delete data
    elif request.method == 'DELETE':
      experiment.delete()
      # delete data "no content"
      return HttpResponse(status=204)
    
    
  
