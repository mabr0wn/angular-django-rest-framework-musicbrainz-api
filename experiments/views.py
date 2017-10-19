from experiments.model import Experiment
from experiments.permission import IsOwnerOrReadOnly
from experiments.serializer import ExperimentSerializer, UserSerializer
from rest_framework import permissions
from rest_framework.decorators import detail_route
from rest_framwork.response import Response
from rest_framework import renderers, viewsets
from django.contrib.auth.models import User

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
    
    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, *kwargs):
        experiment = self.get_object()
        return Response(experiment.highlighted)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
