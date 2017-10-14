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


    
    
  
