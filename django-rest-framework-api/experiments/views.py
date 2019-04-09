# Django
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render
# Django rest
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers, viewsets
# Local
from experiments.models import Experiment
from experiments.serializers import ExperimentSerializer, UserSerializer
# Musicbrainz
import musicbrainzngs as mb
mb.set_useragent('PUT_EMAIL_HERE', version='0.0.1')


class Index(TemplateView):
    template_name = "base.html"


class ExperimentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update', and 'destroy' actions.
    
    additionally we also provide an extra 'highlight' action
    """
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    """
    Notice that we've also used the @detail_route decorator to create a custom action, 
    named highlight. This decorator can be used to add any custom endpoints that don't fit 
    into the standard create/update/delete style.
    
    Custom actions which use the @detail_route decorator will respond to GET requests by 
    default. We can use the methods argument if we wanted an action that responded to POST 
    requests.
    """
    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        experiment = self.get_object()
        return Response(experiment.highlighted)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This Viewset automatically provides 'list' and 'detail' actions
    using the ReadOnly model we know this will provide reas-only
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
