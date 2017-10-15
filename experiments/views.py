from rest_framework import status
from rest_framework.decarators import api_view
from rest_framework.response import Response
from experiments.models import Experiment
from experiments.serializers import ExperimentSerializer


"""
Going to rewrite this method since we do not need to use JSONResponse also it is very unsafe to exempt crsf
use the @api_view decorators instead.

@api_view decorator works with function based views.
"""

@api_views(['GET', 'POST'])
# allows GET and POST methods only.
# Going to add format support suffixes to our API endpoints
# Gives us URLs that explicity reder to a given format. and means our API will be able
# to handle URLs such as 'http://example.com/api/items/4.json'
def experiment_list(request, format=None):
    """
    List all code snippets, or create a new snippet
    """
    if request.method == 'GET':
        # get all the experiment objects
        experiments = Experiment.objects.all()
        # call the fields(many=True)
        serializer = ExperimentSerializer(experiments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # change from data=data to request.data
        serializer = ExperimentSerializer(data=request.data)
        if serializer.is_valid():
            # save it with a 201 http status of created 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # error is not valid
        return Repsonse(serializer.errors, status=status.HTTP._400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def experiment_detail(request, pk, format=None):
    """
    Retrieve, update, or delete a code experiment
    """
    try:
        experiment = Experiment.objects.get(pk=pk)
    except Experiment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ExperimentSerializer(experiment)
        return Response(serialier.data)
    
    elif request.method == 'PUT':
        serializer = ExperimentSerializer(experiment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        experiment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
    
  
