from experiments.model import Experiment, Musician
from experiments.permission import IsOwnerOrReadOnly
from experiments.serializer import ExperimentSerializer, UserSerializer, MusicianSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import detail_route
from rest_framwork.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers, viewsets, mixins
from django.contrib.auth.models import User

from django.shortcuts import render_to_response

import musicbrianzngs as mb

mb.set_useragent('', version='0.0.1')

"""
We can now group all three views classes into one now using
the ViewSet class.
"""
class ExperimentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update', and 'destroy' actions.
    
    additionally we also provide an extra 'highlight' action
    """
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    permission_classes = (permissions.IsAuthenicatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    """
    Notice that we've also used the @detail_route decorator to create a custom action, 
    named highlight. This decorator can be used to add any custom endpoints that don't fit 
    into the standard create/update/delete style.
    
    Custom actions which use the @detail_route decorator will respond to GET requests by 
    default. We can use the methods argument if we wanted an action that responded to POST 
    requests.
    """
    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, *kwargs):
        experiment = self.get_object()
        return Response(experiment.highlighted)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
